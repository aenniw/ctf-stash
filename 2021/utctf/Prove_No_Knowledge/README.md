#### Challenge:

I've been trying to authenticate to this service, but I'm lacking enough information.

`nc crypto.utctf.live 4354`

---

#### Solution:

The challenge's name and description are pointing to [Zero Knoledge proof](https://en.wikipedia.org/wiki/Zero-knowledge_proof). The service hints that we have to fool it 256 times to get the flag. After manual attempts, I assumed that every `odd round` the question will require us to send `r` followed by corresponding `C = g^r mod p` and every `even round` the question will require `r` followed by `(x + r) mod (p - 1)`. The odd rounds are trivial, the even rounds need us to compute `C' = g^r' * (g^x)^-1 mod p` which will hold, when the service will verify for `(C * y) mod p === g^((x+r) mod (p-1)) mod p` since `C'` was crafted by multiplying `g^r'` by modular multiplicative inverse of `y`. For more detailed information refer to [practical examples on the wikipedia](https://en.wikipedia.org/wiki/Zero-knowledge_proof#Practical_examples).

```python
#!/bin/python3

import gmpy2
from pwn import *

global s

if __name__ == '__main__':
    try:
        s = remote('crypto.utctf.live', 4354)
        try:
            print(s.recvuntil('Prove knowledge of x such that g^x mod p = y\n').decode())

            print(s.recvuntil('g:').decode())
            g = int(s.recvline().decode().strip())
            print(g)

            print(s.recvuntil('p:').decode())
            p = int(s.recvline().decode().strip())
            print(p)

            print(s.recvuntil('y:').decode())
            y = int(s.recvline().decode().strip())
            print(y)

            for r in range(128):

                print(s.recvuntil('Pick a random r. Send g^r mod p.').decode())

                gtor = gmpy2.powmod(g, r, p)
                s.sendline(str(gtor))
                print(gtor)

                print(s.recvuntil('Send r.').decode())
                s.sendline(str(r))
                print(str(r))

                print(s.recvuntil('Pick a random r. Send g^r mod p.').decode())
                gr = gmpy2.powmod(g, r, p)
                grr = gmpy2.invert(y, p)
                c = gr * grr
                s.sendline(str(c))
                print(str(c))

                print(s.recvuntil('Send (x + r) mod (p - 1).').decode())
                s.sendline(str(r))
                print(str(r))

            print(s.recvline().decode())
            print(s.recvline().decode())
            print(s.recvline().decode())
        finally:
            s.close()
    except Exception as e:
        raise
```

---

<details><summary>FLAG:</summary>

```text
utflag{questions_not_random}
```

</details>
<br/>
