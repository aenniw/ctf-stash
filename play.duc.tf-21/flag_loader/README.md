#### Challenge:

What more could you ask for than a program that loads the flag for you? Just answer a few simple questions and the flag is yours! [flag_loader](./flag_loader ":ignore")

`nc pwn-2021.duc.tf 31919`

---

#### Solution:

- decompiling reveals that we need to pass 3 checks and then we wait for the flag for `X` seconds based on the result of the check functions

    ```c
    void main()
    {
    char flag[264];
    int iVar1 = check1();
    int iVar2 = check2();
    int iVar3 = check3();

    puts("You\'ve passed all the checks! Please be patient as the flag loads.");
    puts("Loading flag... (this may or may not take a while)");

    sleep(iVar1 * iVar2 * iVar3);

    f = fopen("flag.txt","r");
    fgets(flag,0xff,f);
    printf("%s",flag);
    }
    ```
  - 1. check just reads `5` chars and compares them against static data `DUCTF`
  - 2. check requires us to solve equation `x + y = (rand() & 0xffff)` with few additional conditions, also resulting sleep depends on supplied values
    ```c
    uint check2(void)
    {
    long in_FS_OFFSET;
    uint local_1c;
    uint local_18;
    uint local_14;
    long local_10;
    
    local_10 = *(long *)(in_FS_OFFSET + 0x28);
    local_14 = rand();
    local_14 = local_14 & 0xffff;
    printf("Solve this: x + y = %d\n",(ulong)local_14);
    __isoc99_scanf("%u %u",&local_1c,&local_18);
    if ((((local_1c == 0) || (local_18 == 0)) || (local_1c <= local_14)) || (local_18 <= local_14)) {
        die();
    }
    if ((local_1c + local_18 != local_14) || ((local_18 * local_1c & 0xffff) < 0x3c)) {
        die();
    }
    if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                        /* WARNING: Subroutine does not return */
        __stack_chk_fail();
    }
    return local_18 * local_1c & 0xffff;
    }
    ```
  - 3. check requires us to solve equation `x1 + x2 + x3 + x4 + x5 = (rand() & 0xffff)` with few additional conditions, also resulting sleep depends on supplied values
    ```c
    uint check3(void)
    {
    long in_FS_OFFSET;
    uint local_28;
    uint local_24;
    uint local_20;
    uint local_1c;
    uint local_18;
    uint local_14;
    long local_10;
    
    local_10 = *(long *)(in_FS_OFFSET + 0x28);
    local_14 = rand();
    local_14 = local_14 & 0xffff;
    printf("Now solve this: x1 + x2 + x3 + x4 + x5 = %d\n",(ulong)local_14);
    __isoc99_scanf("%u %u %u %u %u",&local_28,&local_24,&local_20,&local_1c,&local_18);
    if ((((local_28 == 0) || (local_24 == 0)) || (local_20 == 0)) ||
        ((local_1c == 0 || (local_18 == 0)))) {
        die();
    }
    if (((local_24 <= local_28) || (local_20 <= local_24)) ||
        ((local_1c <= local_20 || (local_18 <= local_1c)))) {
        die();
    }
    if ((local_28 + local_24 + local_20 + local_1c + local_18 != local_14) ||
        (((local_18 - local_1c) * (local_20 - local_24) & 0xffff) < 0x3c)) {
        die();
    }
    if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                        /* WARNING: Subroutine does not return */
        __stack_chk_fail();
    }
    return (local_18 - local_1c) * (local_20 - local_24) & 0xffff;
    }
    ```
  - 4. while solving these equation we need to provide the solutions in a way that `result1 * result2 * result3` is ideally zero as this will delay retrieval of the flag

```python
#!/usr/bin/env python3
from pwn import *
import urllib.parse
import base64
import codecs

context.log_level = 'error'

r = remote('pwn-2021.duc.tf', 31919)

# Check 1 ###########################################################

print(r.recvuntil(b"letters:").decode('utf-8').strip())
r.sendline(b"\x44\x55\x43\xab\x47")

# Check 2 ###########################################################

print(r.recvuntil(b"= ").decode('utf-8').strip(), end='')
val = r.recvuntil(b"\n").decode('utf-8').strip()
print(val)

c2 = 0
# Finds solution so that multiplication fo result is zero thus waiting for 0s for flag
for c1 in range(0, 4294967296):
    x = (4294967295 - c1)
    y = (int(val) + 1 + c1)
    offset = (x *  y  & 0xffff)
    if offset > 60 and offset > 10000 and 134217728 % offset == 0:
        c2 = int(134217728 / offset)
        r.sendline(str(x).encode('utf-8'))
        r.sendline(str(y).encode('utf-8'))
        break

# Check 3 ###########################################################

print(r.recvuntil(b"= ").decode('utf-8').strip(), end='')
val = r.recvuntil(b"\n").decode('utf-8').strip()
print(val)

c2 = c2 - 60
xx = [
    (int(val) + 1 - 36 - c2), int(1073741805), int(1073741806), int(1073741830), int(1073741890 + c2),
]
for v in xx:
    r.sendline(str(v).encode('utf-8'))

r.interactive()
```

---

<details><summary>FLAG:</summary>

```
DUCTF{y0u_sur3_kn0w_y0ur_int3gr4l_d4t4_typ3s!}
```

</details>
<br/>
