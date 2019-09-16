#### Challenge:

Soubory PDF mohou obsahovat užitečná data nejen v zobrazeném obsahu. [pdf1.pdf.gz](./pdf1.pdf.gz ":ignore")

---

#### Solution:

```bash
gunzip pdf1.pdf.gz
pdf-parser.py  -o 4 ./pdf1.pdf -d pdf-dump.bin
for c in $( cat ./pdf-dump.bin | grep -i secret | tr '<>' ' ' | awk '{ print $2 }' ); do \
    echo $c | base32 -d 2>/dev/null  | base32 -d; echo; \
done;
```

---

<details><summary>FLAG:</summary>

```
flag{Noam_Chomsky-4081}
```

</details>
