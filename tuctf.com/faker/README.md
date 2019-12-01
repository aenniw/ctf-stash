#### Challenge:

One of these things is not like the other. Can you uncover the flag? [faker](./faker ":ignore")

---

#### Solution:

- just analyze with [ghidra](https://ghidra-sre.org/) and use decompiled sources

```c
#include <stdio.h>
#include <stdlib.h>

void printFlag(char *pcParm1)
{
    char *__dest;
    size_t sVar1;
    int local_30;

    __dest = (char *)malloc(0x40);
    memset(__dest, 0, 0x40);
    strcpy(__dest, pcParm1);
    sVar1 = strlen(__dest);
    local_30 = 0;
    while (local_30 < (int)sVar1)
    {
        __dest[(long)local_30] =
            (char)((int)((((int)__dest[(long)local_30] ^ 0xfU) - 0x1d) * 8) % 0x5f) + ' ';
        local_30 = local_30 + 1;
    }
    puts(__dest);
    return;
}

void thisone(void)
{
    printFlag("\\PJ\\fC|)L0LTw@Yt@;Twmq0Lw|qw@w2$a@0;w|)@awmLL|Tw|)LwZL2lhhL0k");
    return;
}

int main()
{
    thisone();
}

```

---

<details><summary>FLAG:</summary>

```
TUCTF{7h3r35_4lw4y5_m0r3_70_4_b1n4ry_7h4n_m3375_7h3_d3bu663r}
```

</details>
<br/>
