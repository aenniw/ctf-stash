#### Challenge:

Well, this is embarassing...
I've accidentally compiled 999 ELF files with my password somewhere along the line, one character at a time.

Solve these in order, each accepting one ASCII character.
Keep going...eventually combining these solutions will match the regular expression `RITSEC\{.*\}`

Good luck, and thanks for the help! [bottles.tar.lzma](./bottles.tar.lzma ":ignore")

---

#### Solution:

```bash
tar --lzma -xvf bottles.tar.lzma
for f in ./*; do
    for ((i=32;i<127;i++)); do
        printf "\\$(printf %03o "$i")" | ./$f | grep -q  'OK!' && printf "\\$(printf %03o "$i")" && break;
    done
done
```

---

<details><summary>FLAG:</summary>

```
RITSEC{AuT057v}
```

</details>
<br/>
