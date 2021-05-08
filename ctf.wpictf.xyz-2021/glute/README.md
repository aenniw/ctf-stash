#### Challenge:

I swear I didn't realize what I was naming it until I submitted the challenge

![glute.png](./glute.png ":ignore")

---

#### Solution:

We are given PNG image. Looking at it in `binwalk`, I noticed there is PDF at the end of the PNG file (at 285674). I carved it out from the PDF's [Magic bytes](https://en.wikipedia.org/wiki/List_of_file_signatures) till the end of of the file using `dd`. The flag was in it.

```bash
dd if=glute.png of=glute.pdf bs=1 skip=285674
```

---

<details><summary>FLAG:</summary>

```
WPI{P0lyGlOtz_R_koo1}
```

</details>
<br/>
