#### Challenge:

Can you see how this page handles authentication? http://web1.utctf.live:8778

---

#### Solution:

The challenge name hints us to source the site but, the HTML output does not contain anything interesting, but the javascript source does.

```bash
curl http://web1.utctf.live:8778/assets/js/main.js
```

---

<details><summary>FLAG:</summary>

```text
utflag{b33n_th3r3_s0uRc3d_th4t}
```

</details>
<br/>
