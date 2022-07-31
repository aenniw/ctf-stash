#### Challenge:

BBBBBBBBBB BBBBBBBBBB BBBBBBBBBB BBBBBBBBBB BBBBBBBBBB BBBBBBBBBB BBBBBBBBBB BBBBBBBBBB

[chall.jpg](./chall.jpg ":ignore")

---

#### Solution:

We are given corrupted JPEG image. 

Using:

```
hexdump -C BBBBBBBBBB/chall.jpg
```

we see that it contains a lot of `BBBBBBBBBB` strings.

Removing them fixes the file, which holds the flag:

```
perl -pi -e 's/BBBBBBBBBB//g' chall.jpeg
```

---

<details><summary>FLAG:</summary>

```
TFCCTF{the_fl4g_1s_th3_w4y}
```

</details>
<br/>
