#### Challenge:

AES encryption challenge. [aes-ecb.py](./aes-ecb.py ":ignore")

`nc pwn-2021.duc.tf 31914`

---

#### Solution:

```python
#!/usr/bin/python2.7
from pwn import *
import base64

context.log_level = 'error'
r = remote('pwn-2021.duc.tf', 31914)

KEY = ''
found = ''

def submit(msg):
    r.recvuntil("Enter plaintext:\n")
    r.sendline(msg)
    msg =  base64.b64decode(r.recvline())
    return msg

secret = ''

if secret:
    sys.stdout.write(secret)

leaking = True
while leaking:
    offset = 15
    offset_s = 0 + (16 - offset + len(secret)) / 16
    payload = 'X' * ( offset - len(secret) + offset_s * 16)

    base = submit(payload)
    leaking = False
    for c in '!{}_0123456789@ABCDEFGHIJKLMNOPQRSTUVWXYZ"#$%&\'()*+,-./:;<=>?[\]^`|~abcdefghi!jklmnopqrstuvwxyz':
        part = submit(payload + secret + c)
        
        sys.stdout.write(c)
        p1 = part[(16 * (offset_s + 2)):(16 * (1 + (offset_s + 2)))]
        p2 = base[(16 * (offset_s + 2)):(16 * (1 + (offset_s + 2)))]


        if p1 == p2:
            secret += c
            leaking = True
            break
        else:
            sys.stdout.write("\b")

sys.stdout.write("\n")
```

---

<details><summary>FLAG:</summary>

```
DUCTF{ECB_M0DE_K3YP4D_D474_L34k}
```

</details>
<br/>
