#### Challenge:

We went back in time to the late 80s and discovered this mysterious ROM. It seems to be intended to run on a certain Nintendo portable console. I wonder what lies beyond the goal?

Flag is in all caps. [game.gb](./game.gb ":ignore")

---

#### Solution:

- playing the game via [vba-m](https://vba-m.com/) reveals that we need to past multiple walls to reach the flag which could be achieved via `teleport` cheat...
- observing the `memory` as we play reveals that `x` position resides on these addresses `C001 C0A5 C0AA` overriding them to `96` will teleport us the the end of screen allowing us to bypass the wall and reach the flag

- cheat codes for `vba-m`
```
019601C0
0196A5C0
0196AAC0
```

---

<details><summary>FLAG:</summary>

```
UTFLAG{NXHDGZROUT}
```

</details>
<br/>
