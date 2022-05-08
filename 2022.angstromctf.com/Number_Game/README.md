#### Challenge:

Step right up and enter clam's [number game](./number-game ":ignore")! Winners get one (1) free flag!!!

Connect to it at `nc challs.actf.co 31334`.

---

#### Solution:

- quick decompilation via `ghidra` reveals all the "secrets" that we need to input

```c
int main(void)
{
  int iVar1;
  int uVar2;
  size_t sVar3;
  char local_58 [72];
  int local_10;
  int local_c;
  
  puts("Welcome to clam\'s number game!");
  printf("Step right up and guess your first number: ");
  fflush(stdout);
  local_c = read_int();
  if (local_c == 0x12b9b0a1) {
    printf("That\'s great, but can you follow it up? ");
    fflush(stdout);
    local_10 = read_int();
    if (local_10 + local_c == 0x1e996cc9) {
      puts("That was the easy part. Now, what\'s the 42nd number of the Maltese alphabet?");
      getchar();
      fgets(local_58,0x40,stdin);
      sVar3 = strcspn(local_58,"\n");
      local_58[sVar3] = '\0';
      iVar1 = strcmp(local_58,"the airspeed velocity of an unladen swallow");
      if (iVar1 == 0) {
        puts("How... how did you get that? That reference doesn\'t even make sense...");
        puts("Whatever, you can have your flag I guess.");
        print_flag();
        uVar2 = 0;
      }
      else {
        puts("Ha! I knew I would get you there!");
        uVar2 = 1;
      }
    }
    else {
      puts("Sorry but you didn\'t win :(");
      uVar2 = 1;
    }
  }
  else {
    puts("Sorry but you didn\'t win :(");
    uVar2 = 1;
  }
  return uVar2;
}
```

```bash
printf '314159265\n199212072\nthe airspeed velocity of an unladen swallow\n' | nc challs.actf.co 31334
```

---

<details><summary>FLAG:</summary>

```
actf{it_turns_out_you_dont_need_source_huh}
```

</details>
<br/>
