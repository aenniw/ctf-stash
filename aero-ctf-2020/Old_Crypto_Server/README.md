#### Challenge:

We found a very old crypto server.
He has a secret that we want to get.
However, he will not give it up so easily. [main.py](./main.py ":ignore")

`nc tasks.aeroctf.com 44323`

Flag form for this task is `Aero{[0-9a-f]{32}}`

---

#### Solution:

- `AES.MODE_ECB` is performed on 16 byte blocks, as our payload is pre-pended to secret we can guess the secret per `char`
  - encrypt `XXXXXXXXXXXXXXX` -> | `XXXXXXXXXXXXXXXA` | `ero{5013a76ed3b}` | (blocks that will be encrypted) and keep the result
  - encrypt `XXXXXXXXXXXXXXX[a-zA-Z0-9]` and compare first 16 bytes with previous result if they match we have guessed one `char`
  - replace the last `X` in payload with guessed `char` -> `XXXXXXXXXXXXXXA` and repeat

```python
from pwn import *
import base64

context.log_level = 'error'
r = remote('tasks.aeroctf.com', 44323)

KEY = ''
found = ''


def submit(msg):
    r.recv()
    r.sendline('3')
    r.recv()
    r.sendline(msg)
    return base64.b64decode(r.recvline().split("'")[1])


flag = ''

if flag:
    sys.stdout.write(flag)
try:
    while flag[-1:] != '}':
        offset = len(flag) / 16
        payload = 'X' * (15 - len(flag) + offset * 16)
        base = submit(payload)
        for c in '{}_0123456789@abcdefghi!jklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"#$%&\'()*+,-./:;<=>?[\]^`|~':
            part = submit(payload + flag + c)

            sys.stdout.write(c)
            if part[16 * offset:16 * (1 + offset)] == base[16 * offset:16 * (1 + offset)]:
                flag += c
                break
            else:
                sys.stdout.write("\b")
    sys.stdout.write("\n")
except:
    print('\n'+flag)
```

---

<details><summary>FLAG:</summary>

```
Aero{5013a76ed3b98bae1e79169b3495f47a}
```

</details>
<br/>
