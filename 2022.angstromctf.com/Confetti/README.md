#### Challenge:

"From the sky, drop like confetti
All eyes on me, so V.I.P
All of my dreams, from the sky, drop like confetti" - Little Mix
![confetti.png](./confetti.png)

---

#### Solution:

We are given `PNG` file. After running `binwalk` on it, we found out that there are actually `4 images` in the provided file:

```bash
binwalk confetti.pnp
```

```text
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 3971 x 2918, 8-bit/color RGBA, non-interlaced
115           0x73            Zlib compressed data, default compression
967339        0xEC2AB         PNG image, 3971 x 2918, 8-bit/color RGBA, non-interlaced
967454        0xEC31E         Zlib compressed data, default compression
1934678       0x1D8556        PNG image, 3971 x 2918, 8-bit/color RGBA, non-interlaced
1934732       0x1D858C        TIFF image data, big-endian, offset of first image directory: 8
3180408       0x308778        PNG image, 3971 x 2918, 8-bit/color RGBA, non-interlaced
3180523       0x3087EB        Zlib compressed data, default compression
```

Exporting the hidden ones with dd reveals the flag in `flag2.png`:

```bash
dd if=confetti.png of=flag1.png bs=1 skip=967339
dd if=confetti.png of=flag2.png bs=1 skip=1934678
dd if=confetti.png of=flag3.png bs=1 skip=3180408
```

---

<details><summary>FLAG:</summary>

```
actf{confetti_4_u}
```

</details>
<br/>
