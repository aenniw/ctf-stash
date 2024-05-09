#### Challenge:

`nc ecb.utctf.live 9003` [server.py](./server.py ":ignore")

---

#### Solution:

- based on [aero-ctf-2020/Old_Crypto_Server](/aero-ctf-2020/README?id=old_crypto_server)

```python
from pwn import *
import string

context.log_level = 'error'
r = remote('ecb.utctf.live', 9003)

KEY = ''
found = ''


def submit(msg, offset):
    r.recv()
    r.sendline(msg)
    r.recvline()
    return r.recvline().strip()[32 * offset:32 * (1 + offset)]


def get_base(payload, offset):
    bases = []
    while len(bases) != 2:
        base = submit(payload, offset)
        if base not in bases:
            bases.append(base)

    payload = "A" + payload
    base = None
    while base not in bases:
        base = submit(payload, offset)
    bases.remove(base)
    return bases[0]


flag = ''

if flag:
    sys.stdout.write(flag)
while flag[-1:] != '}':
    offset = int(len(flag) / 16)
    payload = 'A' * (15 - len(flag) + offset * 16)

    base = get_base(payload, offset)
    for c in string.printable:
        parts = []
        while len(parts) != 2:
            part = submit(payload + flag + c, offset)
            if part not in parts:
                parts.append(part)

        found = False
        for part in parts:
            sys.stdout.write(c)
            if part == base:
                flag += c
                found = True
                break
            else:
                sys.stdout.write("\b")
        if found:
            break
sys.stdout.write("\n")
```

---

<details><summary>FLAG:</summary>

```
utflag{3cb_w17h_r4nd0m_pr3f1x}
```

</details>
<br/>
