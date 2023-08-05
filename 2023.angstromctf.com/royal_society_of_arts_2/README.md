#### Challenge:

RSA strikes strikes strikes strikes strikes again again again again again!

[rsa2.py](./rsa2.py ":ignore")

`nc challs.actf.co 32400`


---

#### Solution:

RSA `homomorphism` - similar to a previous challenge at `bsidesbos` - [Alice_and_Bob](https://aenniw.github.io/ctf-stash/#/./bsidesbos-2020/README?id=alice_and_bob).

TL;RD: The core principle is this equation:

```
enc(m_1 * m_2) = enc(m_1)*enc(m_2) % N
```


```python
#!/env python3

from Crypto.Util.number import long_to_bytes

import gmpy2
from pwn import *
from struct import *

r = remote('challs.actf.co', 32400)

print(r.recvuntil(b"n = ").decode('utf-8').strip())
n = int(r.recvline().decode('utf-8').strip())
print(n)

print(r.recvuntil(b"e = ").decode('utf-8').strip())
e = int(r.recvline().decode('utf-8').strip())
print(e)

print(r.recvuntil(b"c = ").decode('utf-8').strip())
c = int(r.recvline().decode('utf-8').strip())
print(c)

print(r.recvuntil(b"Text to decrypt: ").decode('utf-8').strip())

multiplier = 2
my_c = pow(multiplier,e,n)
tampered_ciphertext = (my_c * c) % n
r.sendline(str(tampered_ciphertext))

print(r.recvuntil(b"m = ").decode('utf-8').strip())
m = int(r.recvline().decode('utf-8').strip())
print(m)

print(long_to_bytes(m//multiplier))
```

---

<details><summary>FLAG:</summary>

```
actf{rs4_is_sorta_homom0rphic_50c8d344df58322b}
```

</details>
<br/>
