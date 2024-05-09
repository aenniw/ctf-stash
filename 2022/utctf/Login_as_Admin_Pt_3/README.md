#### Challenge:

Ok sorry but just *one* more time. HQ really needs your help. These Web D-EVIL-opers keep changing their site and preventing us from logging in. It seems the one thing they _won't_ change is their username and password \*rolls eyes\*. Can you figure out how to log in?

_FYI, you do *not* need to do the 'Login as Admin' sequence in order, and later parts are not necessarily harder than earlier ones._

[app.py](./app.py ":ignore") `http://web1.utctf.live:2363`

---

#### Solution:

- The form contains hidden param `isAdmin` that needs to be set to `True`.

```bash
curl 'http://web1.utctf.live:2363/'  --data-raw 'username=admin&pwd=admin&isAdmin=True'
```

---

<details><summary>FLAG:</summary>

```
utflag{omg_why_not_upd8_pwd!?!}
```

</details>
<br/>
