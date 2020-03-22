#### Challenge:

Is this enough for you? [main](./main ":ignore")

---

#### Solution:

- decompile with ghidra

```c
undefined8 FUN_001007fa(void)
{
  size_t __n;
  int local_10;
  int local_c;

  write(1,"Welcome to SECURINETS CTF\n",0x1a);
  read(0,&DAT_00301080,0x31);
  __n = strlen(&DAT_00301080);
  (&DAT_0030107f)[__n] = 0;
  local_10 = 0;
  strcpy(&DAT_003010c0,&DAT_00301080);
  __n = strlen(&DAT_00301080);
  memfrob(&DAT_00301080,__n);
  local_c = 0;
  while (local_c < 0x14) {
    local_10 = local_10 +
               (int)(char)((&DAT_00301020)[(long)local_c] ^ (&DAT_00301080)[(long)local_c]);
    local_c = local_c + 1;
  }
  if (local_10 == 0) {
    printf("Good job\nYou can submit with securinets{%s}\n",&DAT_003010c0);
  }
  else {
    puts(":(...");
  }
  return 0;
}
```

- input bytes are via `memfrob` xored with `42` and then compared against bytes at `&DAT_00301020`
- inspect data at address `[ 46h, 19h, 5Eh, 0Dh, 59h, 75h, 5Dh, 1Eh, 58h, 47h, 75h, 1Bh, 5Eh, 75h, 5Fh, 5Ah, 75h, 48h, 45h, 53h ]` and revert process...

```python
print(''.join(map(lambda x: chr(ord(x) ^ 42), 'F\x19^\x0dYu]\x1eXGu\x1b^u_ZuHES')))
```

---

<details><summary>FLAG:</summary>

```
securinets{l3t's_w4rm_1t_up_boy}
```

</details>
<br/>
