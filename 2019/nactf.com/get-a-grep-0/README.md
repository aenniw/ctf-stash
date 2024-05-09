#### Challenge:

Vikram was climbing a chunky tree when he decided to hide a flag on one of the leaves. There are 10,000 leaves so there's no way you can find the right one in time... Can you open up a terminal window and get a grep on the flag? [bigtree.zip](./bigtree.zip ":ignore")

---

#### Solution:

```bash
strings ./bigtree.zip | grep nactf
```

---

<details><summary>FLAG:</summary>

```
nactf{v1kram_and_h1s_10000_l3av3s}
```

</details>
