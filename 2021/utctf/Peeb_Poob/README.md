#### Challenge:

Computers usually go beep boop, but I found this weird computer that goes peeb poob. [peeb_poob](./peeb_poob ":ignore")

---

#### Solution:

- after inspecting the binary with `ghidra` we see that it reads user input, encode it and the compare it with `flag` variable, thus we need to look into `encode` function

```c
undefined4 main(void)
{
  size_t sVar1;
  char acStack52 [32];
  undefined4 local_14;
  uint local_10;
  int local_c;
  
  local_14 = 0;
  local_c = 0;
  while (local_c < 0x20) {
    acStack52[local_c] = '\0';
    local_c = local_c + 1;
  }
  printf("Enter a string: \n");
  fgets(acStack52,0x20,stdin);
  encode(acStack52);
  local_10 = 0;
  while( true ) {
    sVar1 = strlen(acStack52);
    if (sVar1 <= local_10) {
      puts("Nice flag!");
      return 0;
    }
    if (acStack52[local_10] != flag[local_10]) break;
    local_10 = local_10 + 1;
  }
  puts("Wrong!");
                    /* WARNING: Subroutine does not return */
  exit(-1);
}
```

- this function just encodes input string with `XOR` thus we can easily decode the `flag` by reversing the bytes `54h, 27h, 62h, Bh, 4Bh, 2Bh, 73h, 14h, 6h, 32h, 61h, 3Bh, 78h, 4Fh, 5Ch, 29h, 57h, 20h, 30h,  6h, 45h, 1Dh, 4Eh, 7Bh, 6Ah, Fh, 51h, 5Eh` 

```c
void encode(char *param_1)
{
  size_t sVar1;
  uint uVar2;
  uint local_10;
  
  local_10 = 0;
  while (sVar1 = strlen(param_1), local_10 < sVar1) {
    uVar2 = (uint)((int)local_10 < 0);
    uVar2 = ((local_10 ^ -uVar2) + uVar2 & 3 ^ -uVar2) + uVar2;
    if (uVar2 < 4) {
      switch(uVar2) {
      case 0:
        param_1[local_10] = param_1[local_10] ^ 0x21;
        break;
      case 1:
        param_1[local_10] = param_1[local_10] ^ 7;
        break;
      case 2:
        param_1[local_10] = param_1[local_10] ^ 0x23;
        break;
      case 3:
        param_1[local_10] = param_1[local_10] ^ 5;
      }
    }
    sVar1 = strlen(param_1);
    if (local_10 + 1 < sVar1) {
      param_1[local_10 + 1] = param_1[local_10] ^ param_1[local_10 + 1];
    }
    local_10 = local_10 + 1;
  }
  return;
}
```

```c
#include <stdio.h>
#include <string.h>

char flag[] = {0x54, 0x27, 0x62, 0xB, 0x4B, 0x2B, 0x73, 0x14, 0x6, 0x32, 0x61, 0x3B, 0x78, 0x4F, 0x5C, 0x29, 0x57, 0x20, 0x30, 0x6, 0x45, 0x1D, 0x4E, 0x7B, 0x6A, 0xF, 0x51, 0x5E, 0x0, 0x0, 0x0, 0x0};

int main()
{
    char decoded;
    size_t input_len;
    unsigned int i = 0;
    while (input_len = strlen(flag), i < input_len)
    {
        unsigned int switcher = (unsigned int)((int)i < 0);
        switcher = ((i ^ -switcher) + switcher & 3 ^ -switcher) + switcher;
        if (switcher < 4)
        {
            switch (switcher)
            {
            case 0:
                decoded = flag[i] ^ 0x21;
                break;
            case 1:
                decoded = flag[i] ^ 7;
                break;
            case 2:
                decoded = flag[i] ^ 0x23;
                break;
            case 3:
                decoded = flag[i] ^ 5;
            }
        }
        if (i > 0)
        {
            decoded = flag[i - 1] ^ decoded;
        }
        printf("%c", decoded);
        i = i + 1;
    }
    return 0;
}
```

---

<details><summary>FLAG:</summary>

```
utflag{b33p_b00p_p33b_p00b}
```

</details>
<br/>
