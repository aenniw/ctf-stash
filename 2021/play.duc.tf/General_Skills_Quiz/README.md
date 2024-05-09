#### Challenge:

QUIZ TIME! Just answer the questions. Pretty easy right?

`nc pwn-2021.duc.tf 31905`

---

#### Solution:

```python
#!/usr/bin/env python3
from pwn import *
import urllib.parse
import base64
import codecs

context.log_level = 'error'

r = remote('pwn-2021.duc.tf', 31905)

print(r.recvuntil(b"quiz...").decode('utf-8').strip())
r.sendline(b"")

print(r.recvuntil(b"1+1=?").decode('utf-8').strip())
r.sendline(b'2')

print(r.recvuntil(b"(base 10): ").decode('utf-8').strip(), end='' )
value = r.recvuntil(b"\n").decode('utf-8').strip()
print(value)
r.sendline(str(int(value, 16)).encode('utf-8'))


print(r.recvuntil(b"letter: ").decode('utf-8').strip(), end='' )
value = r.recvuntil(b"\n").decode('utf-8').strip()
print(value)
r.sendline(chr(int(value, 16)).encode('utf-8'))

print(r.recvuntil(b"symbols: ").decode('utf-8').strip(), end='' )
value = r.recvuntil(b"\n").decode('utf-8').strip()
print(value)
r.sendline(urllib.parse.unquote(value).encode('utf-8'))

print(r.recvuntil(b"plaintext: ").decode('utf-8').strip(), end='' )
value = r.recvuntil(b"\n").decode('utf-8').strip()
print(value)
r.sendline(base64.b64decode(value))

print(r.recvuntil(b"Base64: ").decode('utf-8').strip(), end='' )
value = r.recvuntil(b"\n").decode('utf-8').strip()
print(value)
r.sendline(base64.b64encode(value.encode('utf-8')))

print(r.recvuntil(b"plaintext: ").decode('utf-8').strip(), end='' )
value = r.recvuntil(b"\n").decode('utf-8').strip()
print(value)
r.sendline(codecs.encode(value, 'rot_13').encode('utf-8'))

print(r.recvuntil(b"equilavent: ").decode('utf-8').strip(), end='' )
value = r.recvuntil(b"\n").decode('utf-8').strip()
print(value)
r.sendline(codecs.encode(value, 'rot_13').encode('utf-8'))

print(r.recvuntil(b"(base 10): ").decode('utf-8').strip(), end='' )
value = r.recvuntil(b"\n").decode('utf-8').strip()
print(value)
r.sendline(str(int(value,2)).encode('utf-8'))

print(r.recvuntil(b"equivalent: ").decode('utf-8').strip(), end='' )
value = r.recvuntil(b"\n").decode('utf-8').strip()
print(value)
r.sendline('0b{0:08b}'.format(int(value)).encode('utf-8'))

print(r.recvuntil(b"universe?").decode('utf-8').strip(), end='' )
r.sendline(b'DUCTF')


r.interactive()
```

---

<details><summary>FLAG:</summary>

```
DUCTF{you_aced_the_quiz!_have_a_gold_star_champion}
```

</details>
<br/>
