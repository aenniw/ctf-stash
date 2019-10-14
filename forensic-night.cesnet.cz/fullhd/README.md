#### Challenge:

Opravdu kvalitní obrázek. [flag.bmp.gz](./flag.bmp.gz ":ignore")

---

#### Solution:

- update bmp header so that image size is 1920x1080 [BMP_file_format](https://en.wikipedia.org/wiki/BMP_file_format)

| Offset (hex) | Offset (dec) | Size (bytes) |                 Description                  |
| :----------: | :----------: | :----------: | :------------------------------------------: |
|      0E      |      14      |      4       |    the size of this header, in bytes (40)    |
|      12      |      18      |      4       | the bitmap width in pixels (signed integer)  |
|      16      |      22      |      4       | the bitmap height in pixels (signed integer) |

```console
00000000   42 4D 86 91  00 00 00 00  00 00 36 00  00 00 28 00  00 00 80 07  00 00 38 04  00 00 01 00  18 00 00 00  00 00 50 91  00 00 00 00  BM........6...(.......8...........P.....
```

---

<details><summary>FLAG:</summary>

```
flag{Alan_Turing-5368}
```

</details>
