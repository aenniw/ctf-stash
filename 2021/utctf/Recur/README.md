#### Challenge:

I found this binary that is supposed to print flags.

It doesn't seem to work properly though... [recur](./recur ":ignore")

---

#### Solution:


- after inspecting the binary with `ghidra` we see that it decodes `flag` via `XOR` with recursively generated value thus greatly reducing the decode speed after few characters...

```c
undefined8 main(void)
{
  byte bVar1;
  byte bVar2;
  int local_1c;
  
  local_1c = 0;
  while (local_1c < 0x1c) {
    bVar1 = flag[local_1c];
    bVar2 = recurrence();
    putchar((int)(char)(bVar2 ^ bVar1));
    fflush(stdout);
    local_1c = local_1c + 1;
  }
  return 0;
}

int recurrence(int param_1)
{
  int iVar1;
  int iVar2;
  
  if (param_1 == 0) {
    iVar1 = 3;
  }
  else {
    if (param_1 == 1) {
      iVar1 = 5;
    }
    else {
      iVar1 = recurrence(param_1 + -1);
      iVar2 = recurrence(param_1 + -2);
      iVar1 = iVar2 * 3 + iVar1 * 2;
    }
  }
  return iVar1;
}
```

- by adding `std::map` as cache to `recurrence` function we can speed up the decode process enough to see the whole flag

```cpp
#include <stdio.h>
#include <map>

int flag[] = {0x76, 0x71, 0xc5, 0xa9, 0xe2, 0x22, 0xd8, 0xb5, 0x73, 0xf1, 0x92, 0x28, 0xb2, 0xbf, 0x90, 0x5a, 0x76, 0x77, 0xfc, 0xa6, 0xb3, 0x21, 0x90, 0xda, 0x6f, 0xb5, 0xcf, 0x38};

unsigned long recurrence(int nesting)
{
    static std::map<int, unsigned long> lookup;
    if (lookup.find(nesting) != lookup.end())
    {
        return lookup[nesting];
    }

    unsigned long result;
    unsigned long recur_1;
    unsigned long recur_2;

    if (nesting == 0)
    {
        result = 3;
    }
    else
    {
        if (nesting == 1)
        {
            result = 5;
        }
        else
        {
            recur_1 = recurrence(nesting + -1);
            recur_2 = recurrence(nesting + -2);
            result = (unsigned long)(unsigned int)((int)recur_2 * 3 + (int)recur_1 * 2);
        }
    }

    lookup[nesting] = result;
    return result;
}

int main()
{

    int i = 0;
    while (i < 0x1c)
    {
        char flag_char = flag[(long)i];
        unsigned long _xor_key = recurrence(i * i);
        putchar((int)(char)((char)_xor_key ^ flag_char));
        fflush(stdout);
        i = i + 1;
    }
    return 0;
}
```

---

<details><summary>FLAG:</summary>

```
utflag{0pt1m1z3_ur_c0d3_l0l}
```

</details>
<br/>
