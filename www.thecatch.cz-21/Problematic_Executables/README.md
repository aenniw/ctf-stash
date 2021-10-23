#### Challenge:

Hi Expert, 

some unhappy archaeologist tells you about her problems with examination of some executable - it always ends with `Alarm! Bad usage! Alarm!`. Luckily, part of the original code was retrieved, but no cuneiform, hieroglyphs or cat pictures were present, so the archaeologist cannot understand it. Prove you skill and found how to run the executable. 

Download the file [`executables.zip`](./executables.zip ":ignore")

---

#### Solution:

- based on the source provided we known the arguments of the executable, only thing left is to figure out the right key...

```c
int main(int argc, char *argv[]) {
  int num;

  if (argc != 4){
    printf("Alarm! Bad usage! Alarm!\n");
    return 1;
  }
  if (strcmp(argv[1], "show-me-the-secret") != 0 || strcmp(argv[2], "please") != 0){
    printf("Alarm! Bad usage! Alarm!\n");
    return 1;
  }
  num = atoi(argv[3]);
  if (num < 4 || num > 7){
    printf("Alarm! Bad usage! Alarm!\n");
    return 1;
  }

  print_secret(num);
  return 0;
}
```

```bash
for i in {4..7}; do
    ./executable 'show-me-the-secret' 'please' ${i}
done
```

---

<details><summary>FLAG:</summary>

```
FLAG{mbK4-xd0U-cNip-36tm}
```

</details>
<br/>
