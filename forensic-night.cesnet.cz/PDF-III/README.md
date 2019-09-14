#### Challenge:

PDF je renderováno stránku po stránce a sestává z mnoha objektů. Na prohlížení lze použít například `pdf-parser`:

https://blog.didierstevens.com/programs/pdf-tools/

[pdf3.pdf.gz](./pdf3.pdf.gz ':ignore')

---

#### Solution:

```bash
pdf-parser.py -o 17 ./pdf3.pdf -d pdf-dump.bin
binwalk -Me pdf-dump.bin
grep "flag" ./_pdf-dump.bin.extracted/*
```

---

<details><summary>FLAG:</summary>

```
flag{Jack_Dorsey-6302}
```

</details>
