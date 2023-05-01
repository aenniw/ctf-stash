#### Challenge:

My friend sent me this [town simulator](./TOWN.8xp ":ignore"). I can't seem to beat it. Can you help me?

---

#### Solution:

- provided file seems to be binary that could be executed on [TI-83+ calculators](https://www.cemetech.net/projects/jstified/), however executing ti seems to be rabbit hole...
- after inspecting the binary there seems to be an interesting string the the actual messages printed out `3331262a37297532381a7d751a7136327224212e052b652f` that doesn't match anything around that could be XORed flag
- after trying to brute-force the flag with known `crib=actf` on `CyberChef` we find out that the `XOR` key  begins with 3 same values, with this knowledge and some guess work we get to the actual key `525252 4c4c4c 414141 454545 454545 414141 4c4c4c 525252`

---

<details><summary>FLAG:</summary>

```
actf{e4sy_80_4ss3embIy7}
```

</details>
<br/>
