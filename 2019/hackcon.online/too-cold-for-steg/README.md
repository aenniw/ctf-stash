#### Challenge:

The challenge name is enough for you to solve it. Everything you need is present in the text file. [final.txt.tar.lzma](./final.txt.tar.lzma ":ignore")

---

#### Solution:

```bash
tar --lzma -xvf final.txt.tar.lzma
grep  "d4rk" final.txt # cells_--are sometimes found, particularly [password is : d4rkc0de-IIITD ]when resistant substances
stegsnow -C -p d4rkc0de-IIITD final.txt
```

---

<details><summary>FLAG:</summary>

```
d4rk{h@ving_fun_w1th_st3gsn0w?}c0de
```

</details>
