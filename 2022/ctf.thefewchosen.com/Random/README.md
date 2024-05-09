#### Challenge:

I created a random number generator as a project. Unfortunately it only has one option, but I will add more soon (or not)!

[random](./random ":ignore")

---

#### Solution:

- inspecting binary via `ghidra` reveals what input needs to by supplied

```c
int main(void) {
  uint uVar1;
  time_t tVar2;
  char *pcVar3;
  int local_14;
  
  tVar2 = time((time_t *)0x0);
  srand((uint)tVar2);
  puts("Menu: \n1. Generate number");
  __isoc99_scanf(&DAT_0010201e,&local_14);
  if (local_14 == 1) {
    uVar1 = rand();
    printf("%d",(ulong)uVar1);
  }
  else if (local_14 == 1337) {
    pcVar3 = getenv("FLAG");
    printf("%s",pcVar3);
  }
  else {
    printf("wrong option");
  }
  return 0;
}
```

```bash
echo 1337 | nc 01.linux.challenges.ctf.thefewchosen.com 59762
```

---

<details><summary>FLAG:</summary>

```
TFCCTF{Th3r3_w3r3_m0r3_0pt10n5_4ft3r_4ll!}
```

</details>
<br/>
