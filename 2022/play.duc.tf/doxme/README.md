#### Challenge:

Office is my safe word... [doxme](./doxme ":ignore")

---

#### Solution:

Running `file` command says its `Microsoft OOXML`, considering the name of the challenge and its description, just renaming it to `doxme.docx` and opening it reveals `first half of the flag` as image, but second is nowhere to be found.

Using `binwalk` on it I noticed:

```
3856          0xF10           Zip archive data, at least v2.0 to extract, compressed size: 4038, uncompressed size: 9430, name: word/media/image1.png
7973          0x1F25          Zip archive data, at least v2.0 to extract, compressed size: 3278, uncompressed size: 8812, name: word/media/image2.png
```

Running `unzip doxme.docx` and checking the paths `./word/media/image1.png` and `./word/media/image2.png` gives the whole flag.

---

<details><summary>FLAG:</summary>

```
DUCTF{WOrd_D0Cs_Ar3_R34L1Y_W3ird}
```

</details>
<br/>
