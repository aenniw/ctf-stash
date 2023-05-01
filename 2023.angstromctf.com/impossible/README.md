#### Challenge:

Is this challenge impossible? `nc challs.actf.co 32200`

[impossible.py](./impossible.py ":ignore")

---

#### Solution:

- inspecting the code reveals that if we get `one_encoding` or `zero_encoding` functions to return empty array we get the flag
  - `one_encoding` check just the first `64` bits if there is non zero bit so we can supply `0b10000000000000000000000000000000000000000000000000000000000000000` and get the flag 

---

<details><summary>FLAG:</summary>

```
actf{se3ms_pretty_p0ssible_t0_m3_7623fb7e33577b8a}
```

</details>
<br/>
