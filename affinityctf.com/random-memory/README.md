#### Challenge:

nc 159.89.22.33 5566

---

#### Solution:

- python2 wont work, python3 is required as runtime

```python
#!/usr/bin/python3
from pwn import *
import random


def rcv():
    return s.recvline().decode('utf-8').strip()


def rcvu(msg):
    return s.recvuntil(msg).decode('utf-8').strip()


s = remote('159.89.22.33', 5566)
print(rcvu('System booted'))
msg = rcv()
random.seed(float(msg.split(',')[0][1:-1]))

msg = rcvu('NULL')
addr = int(msg.split('\n')[-1:][0].split(':')[0], 16)
rcvu('Set value:')
for i in range(addr + 1):
    value = hex(random.randint(0, 31337))
    if i == addr:
        s.sendline(value)
print(rcvu('}'))

```

---

<details><summary>FLAG:</summary>

```
AFFCTF{d0n7_l0s3_y0ur_m3m0ry}
```

</details>
