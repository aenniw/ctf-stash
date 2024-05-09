#### Challenge:

That data? No it's long gone. It's basically history [http://us-central-1.ritsec.club/l/chromebin](https://drive.google.com/uc?export=view&id=1ff3A5fmY0PBwTm6HBKC-5MqbBsCXJv1t)

---

#### Solution:

```bash
unlzma chromebin.lzma
strings ./chromebin | grep -i ritsec
curl "us-central-1.ritsec.club/l/relaxfizzblur"
```

---

<details><summary>FLAG:</summary>

```
RITSEC{SP00KY_BR0WS3R_H1ST0RY}
```

</details>
<br/>
