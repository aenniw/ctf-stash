#### Challenge:

Ah yes, the beautiful harp! A family member of such a wonderful type of musical instruments! [harp.jpg](./harp.jpg ":ignore")

---

#### Solution:

```console
binwalk harp.jpg

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
143651        0x23123         JPEG image data, JFIF standard 1.01
```

```bash
dd if=harp.jpg of=h-1.jpg bs=1 count=143651
strings h-1.jpg | sed -r "s/\s//g ; s/^(.{7})(.).*$/\2/" | tr -d '\n'
```

---

<details><summary>FLAG:</summary>

```
flag{the_harp_instrument_has_vertical_strings}
```

</details>
<br/>
