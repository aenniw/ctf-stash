#### Challenge:

The boys back at HQ need you again! The Web D-EVIL-opers have changed their login page a bit, but we suspect the admin username and password are STILL set to `admin`. We're having trouble submitting the credentials, though. Can you help us out?

_FYI, you do *not* need to do the 'Login as Admin' sequence in order, and later parts are not necessarily harder than earlier ones._
[app.py](./app.py ":ignore") `http://web1.utctf.live:2362`

---

#### Solution:

- Button was disabled, but we are using `curl` anyway, so ...

```bash
curl 'http://web1.utctf.live:2362/' --data-raw 'username=admin&pwd=admin'
```

---

<details><summary>FLAG:</summary>

```
utflag{*re@lly*gott@_upd8_th@t_pwd}
```

</details>
<br/>
