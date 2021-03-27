#### Challenge:

My buddy Francis is *really* into Bacon. He loves it so much that he gave me this encoded bacon-themed flag (he said he was inspired by the sound of sizzling bacon).

```
sSsSSsSSssSSsSsSsSssSSSSSSSssS{SSSsSsSSSsSsSSSsSSsSSssssssSSSSSSSsSSSSSSSSsSSsssSSssSsSSSsSSsSSSSssssSSsssSSsSSsSSSs}
```

---

#### Solution:

After googling I found there exists (Baconian cipher)[https://www.dcode.fr/bacon-cipher], so I converted the input `S -> A; s->B` and used this site to get the flag.

```bash
echo "sSsSSsSSssSSsSsSsSssSSSSSSSssSSSSsSsSSSsSsSSSsSSsSSssssssSSSSSSSsSSSSSSSSsSSsssSSssSsSSSsSSsSSSSssssSSsssSSsSSsSSSs" | sed s/S/A/g | sed s/s/B/g
```

---

<details><summary>FLAG:</summary>

```text
utflag{crispybaconcipher}
```

</details>
<br/>
