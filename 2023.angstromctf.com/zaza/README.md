#### Challenge:

Bedtime! `nc challs.actf.co 32760`

[zaza](./zaza ":ignore")

---

#### Solution:

- reversing the binary in `ghidra` reveals that we need to provide correct input 3 times
- the first one is pretty simple we'll just pass `4919`
```c
  input = 0;
  multiplier = 0;
  printf("I\'m going to sleep. Count me some sheep: ");
  __isoc99_scanf("%d",&input);
  if (input != 4919) {
    puts("That\'s not enough sheep!");
    exit(1);
  }
```
- the second is similar as we just need to solve equation `(4919 * x) mod 4294967295 = 1`, for that we can use [wolframalpha](https://www.wolframalpha.com/input?i=%284919+*+x%29+mod+4294967295+%3D+1) and just pass `3977144954`
```c
  printf("Nice, now reset it. Bet you can\'t: ");
  __isoc99_scanf("%d",&multiplier);
  if (multiplier * input == 1) {
    printf("%d %d",(ulong)multiplier,(ulong)(input + multiplier));
    puts("Not good enough for me.");
    exit(1);
  }
```
- the last one we need to reverse the xor key and return it back
```c
  puts("Okay, what\'s the magic word?");
  getchar();
  fgets(input,64,stdin);
  input_len = strcspn(input,"\n");
  input[input_len] = '\0';
  xor_(input);
  iVar1 = strncmp(input,"2& =$!-( <*+*( ?!&$$6,. )\' $19 , #9=!1 <*=6 <6;66#",0x32);
  if (iVar1 != 0) {
    puts("Nope");
    exit(1);
  }
```
- for that we can just reuse the decompiled `xor_` function and get the correct input back like so and pass `SHEEPSHEEPSHEEPSHEEPSHEEPSHEEPSHEEPSHEEPSHEEPSHEEP`
```c
#include <stdio.h>
#include <string.h>

void xor_(char *param_1)
{
    char xor_key[] = "anextremelycomplicatedkeythatisdefinitelyuselessss";
    int sVar1 = 0;
    int local_24 = 0;
    while (1)
    {
        sVar1 = strlen(xor_key);
        if (sVar1 <= local_24)
            break;
        param_1[local_24] = param_1[local_24] ^ xor_key[local_24];
        local_24 = local_24 + 1;
    }
    return;
}

void main()
{
    char key[] = "2& =$!-( <*+*( ?!&$$6,. )\' $19 , #9=!1 <*=6 <6;66#";

    xor_(key);
    printf("%s", key);
}
```

---

<details><summary>FLAG:</summary>

```
actf{g00dnight_c7822fb3af92b949}
```

</details>
<br/>
