#### Challenge:

Someone sent me this file ([mysterious.txt](./mysterious.txt ':ignore')) .It contains only ><+-.,[] symbols and no other letters or numbers.

---

#### Solution:

https://en.wikipedia.org/wiki/Brainfuck
https://en.wikipedia.org/wiki/Esoteric_programming_language#Malbolge

```bash
# branfuck          | malbolge | decode hex | reverse chars
bf ./mysterious.txt | malbolge | xxd -r -p | tac -r -s 'x\|[^x]'
```

---

<details><summary>FLAG:</summary>

```
d4rk{e50t3r1c_lAnguAg3_w1th_c@f3_b@b3_@t_1t5_b35t}c0de
```

</details>
