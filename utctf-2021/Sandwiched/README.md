#### Challenge:

I got this super confidential document that is supposed to have secret information about the flag, but there's nothing useful in the PDF!

[secret.pdf](./secret.pdf ":ignore")

---

#### Solution:

Running `binwalk` on the provided file shows embeded JPEG:

```text
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PDF document, version: "1.5"
71            0x47            Zlib compressed data, default compression
290           0x122           Zlib compressed data, default compression
6252          0x186C          Zlib compressed data, default compression
7824          0x1E90          JPEG image data, JFIF standard 1.01
37768         0x9388          PDF document, version: "1.5"
...
```

Carving it out:

```bash
dd if=./secret.pdf of=out.jpg bs=1 skip=7824 count=29944
```

Note that the JPEG is malformed (It is lacking ending JPEG magic bytes `FFD9`), but it still can be opened in some viewers including Chrome browser to read the flag.

---

<details><summary>FLAG:</summary>

```text
utflag{file_sandwich_artist}
```

</details>
<br/>
