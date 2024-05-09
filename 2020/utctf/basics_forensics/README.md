#### Challenge:

My friend said they hid a flag in this picture, but it's broken! Now that I think about it, I don't even know if it really is a picture... [secret.jpeg.tar.lzma](./secret.jpeg.tar.lzma ":ignore")

---

#### Solution:

```bash
strings secret.jpeg | grep -i 'utflag'
```

---

<details><summary>FLAG:</summary>

```
utflag{fil3_ext3nsi0ns_4r3nt_r34l}
```

</details>
<br/>
