#### Challenge:

Hmmmm, this strange program seems to be contacting a command and control server. Why?

[xf1ltr80r](./xf1ltr80r ":ignore")

---

#### Solution:

Since this was a `rev` challenge, I opened the file in `ghydra`. In `main`, there was a function `genDataToExfiltrate`, which was building a string out of `hex` constants using some array addressing shenaningans.
I decided, that fastest way to get the flag is to reimplement it in `C`. The flag was also base64 encoded, which can be seen from a far based on the `0x3D3D` value in hex).

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

// https://helloacm.com/the-c-function-to-print-a-char-array-string-in-hexadecimal/
void printCharInHexadecimal(const char* str, int len) {
  for (int i = 0; i < len; ++ i) {
    uint8_t val = str[i];
    char tbl[] = "0123456789ABCDEF";
    // printf("0x");
    printf("%c", tbl[val / 16]);
    printf("%c", tbl[val % 16]);
    // printf(" ");
  }
  printf("\n");
}


int main() {
  uint32_t *__s;
  size_t sVar1;

  __s = (uint32_t *)malloc(0x100);
  *__s = 0x423156;
  *(uint32_t *)((long)__s + 3) = 0x7a654a;
  *(uint32_t *)((long)__s + 6) = 0x64344e;
  *(uint32_t *)((long)__s + 9) = 0x7a4948;
  __s[3] = 0x4e5462;
  *(uint32_t *)((long)__s + 0xf) = 0x566573;
  *(uint32_t *)((long)__s + 0x12) = 0x497539;
  *(uint32_t *)((long)__s + 0x15) = 0x6b4a33;
  __s[6] = 0x385665;
  *(uint32_t *)((long)__s + 0x1b) = 0x7a4d78;
  *(uint32_t *)((long)__s + 0x1e) = 0x4e334d;
  *(uint32_t *)((long)__s + 0x21) = 0x7a4158;
  __s[9] = 0x74474e;
  *(uint32_t *)((long)__s + 0x27) = 0x674339;
  *(short *)((long)__s + 0x2a) = 0x3d3d;
  *(char *)(__s + 0xb) = 0;
  sVar1 = strlen((char *)__s);
  *(uint32_t *)(sVar1 + (long)__s) = 0xa0d0a0d;
  *(char *)((uint32_t *)(sVar1 + (long)__s) + 1) = 0;

  // Print resulting hex string
  printCharInHexadecimal(__s, 0x100);
```

---

<details><summary>FLAG:</summary>

```
WPI{3xtr3m3ly_n#rdy_13375p34k}
```

</details>
<br/>
