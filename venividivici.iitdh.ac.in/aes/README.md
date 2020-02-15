#### Challenge:

A Intern at MI 6 thought this was a good idea!! [aes.py](./aes.py ":ignore")

`nc ctf.iitdh.ac.in 2201`

---

#### Solution:

```python
#!/usr/bin/python3
from pwn import *
import random


def encrypt(c=""):
    s = remote('ctf.iitdh.ac.in', 2201)
    s.recvuntil('decrypt - decrypt a message').decode('utf-8').strip()
    s.sendline("encrypt")
    s.recvline().decode('utf-8').strip()
    s.sendline("signature=Parsec"+c)
    msg = s.recvline().decode('utf-8').strip().split(' ')[1]
    return msg

context.log_level = 'error'
length = len(encrypt())

flag=""
while flag[-1:] != '}':
    for c in '{}_0123456789@abcdefghi!jklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"#$%&\'()*+,-./:;<=>?[\]^`|~':
        sys.stdout.write(c)
        if len(encrypt(flag + c)) == length:
            flag += c
            break
        else:
            sys.stdout.write("\b")

print("Parsec" +flag)
```

---

<details><summary>FLAG:</summary>

```
Parsec{c0mpr3ssion_i$_@_b!*cH}
```

</details>
<br/>
