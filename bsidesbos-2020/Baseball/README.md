#### Challenge:

I found this baseball... but... it doesn't really look like a baseball? [baseball](./baseball ":ignore")

---

#### Solution:

- [CyberChef](https://gchq.github.io/CyberChef/#input=%5Bobject%20Object%5D,%5Bobject%20Object%5D,%5Bobject%20Object%5D)

```json
[
  { "op": "From Base64",
    "args": ["A-Za-z0-9+/=", true] },
  { "op": "From Base32",
    "args": ["A-Z2-7=", true] },
  { "op": "From Base58",
    "args": ["123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz", true] }
]
```

---

<details><summary>FLAG:</summary>

```
flag{wow_you_hit_a_homerun_and_really_ran_the_bases_there}
```

</details>
<br/>
