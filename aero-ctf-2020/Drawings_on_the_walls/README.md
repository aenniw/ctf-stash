#### Challenge:

My friend started having problems with his head and he began to draw some nonsense on the walls.

Can you make out these notes?

<a href="https://mega.nz/#!WJ4mGaBB!tW9Ls1Zlx-LBhUiEqVfWajUqTy9UT5lJk44jYqvBx_w">memory.tgz</a>

---

#### Solution:

```bash
volatility -f memory.dmp imageinfo
volatility -f memory.dmp --profile=Win10x64 pslist
volatility -f memory.dmp --profile=Win10x64 memdump -p 2080 -D ./
mv ./2080.dmp ./2080.data
```

- in [Gimp](https://www.gimp.org/) open process memory and slowly check data via updating `possition` and `width` for screens of `mspaint`

---

<details><summary>FLAG:</summary>

```
Aero{g00dj0b_y0u_f1n411y_g07_7h3_wh0l3_fl4g}
```

</details>
<br/>
