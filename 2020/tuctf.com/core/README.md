#### Challenge:

We were able to recover a few files we need analyzed. Think you can get anything outta these? [core](./core ":ignore"), [run.c](./run.c ":ignore")

---

#### Solution:

- reuse source for encryption/decryption

```c
#include <stdio.h>
#include <string.h>

void xor (char *str, int len) {
    for (int i = 0; i < len; i++)
    {
        str[i] = str[i] ^ 1;
    }
    printf("%s\n", str);
}

    int main(int argc, char **argv)
{
    setvbuf(stdout, NULL, _IONBF, 20);
    setvbuf(stdin, NULL, _IONBF, 20);

    xor(argv[1], strlen(argv[1]));

    return 0;
}
```

- since its encrypted as XOR encrypt `TUCTF{` and look for resulting string in binary

```bash
gcc solve.c -o solve
strings ./core | grep "$(./solve 'TUCTF{')" # UTBUGzb1s2^etlq>^O2w2s^i25se^1g^x1t|
./solve 'UTBUGzb1s2^etlq>^O2w2s^i25se^1g^x1t|'
```

---

<details><summary>FLAG:</summary>

```
TUCTF{c0r3_dump?_N3v3r_h34rd_0f_y0u}
```

</details>
<br/>
