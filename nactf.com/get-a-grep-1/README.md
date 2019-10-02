#### Challenge:

Juliet hid a flag among 100,000 dummy ones so I don't know which one is real! But maybe the format of her flag is predictable? I know sometimes people add random characters to the end of flags... I think she put 7 random vowels at the end of hers. Can you get a GREP on this flag? [flag.txt](./flag.txt ":ignore")

---

#### Solution:

```bash
grep -E 'nactf{.*(a|A|e|E|i|I|o|O|u|U|y|Y){7}}' ./flag.txt
```

---

<details><summary>FLAG:</summary>

```
nactf{r3gul4r_3xpr3ss10ns_ar3_m0r3_th4n_r3gul4r_euaiooa}
```

</details>
