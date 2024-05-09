#### Challenge:

Can you find the real mines!!! [minesweeper](./minesweeper ":ignore")

`nc ctf.iitdh.ac.in 2200`

---

#### Solution:

- suspicious `ro.data` in binary found... extracted all that may be base64 encoded and `len == 4`

```bash
for c in UEg4 ZWJp V1Z2 b20v aHR0 cHM6 c0I= Ly9w YXN0 bi5j; do
    echo -n $c | base64 -d
    echo
done
```

- https://pastebin.com/PH8WVvsB

---

<details><summary>FLAG:</summary>

```
Parsec{C0nGratsss_y0u_R_Aa_GameR}
```

</details>
<br/>
