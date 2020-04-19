#### Challenge:

They say the full moon makes people go crazy... hopefully this stego won't have the same effect on you!

[Luna.tar.xz](./Luna.tar.xz ":ignore")

---

#### Solution:

```bash
binwalk -Me jut
cat _jut.extracted/2D # decode hex
binwalk -Me  jut.exif
dd if=jut.exif of=jut.jpg bs=1 skip=420
```

---

<details><summary>FLAG:</summary>

```
WPI{M00N_mOOn}
```

</details>
<br/>
