#### Challenge:

Jak v PDF opravit chybu? Snadno! [pdf2.pdf.gz](./pdf2.pdf.gz ':ignore')

---

#### Solution:

- pdf contains multiple `%%EOF` at the end which points to incremental PDF
- remove appended section of PDF

```console
trailer
<</Size 246 /Root 243 0 R>>
startxref
28851
%%EOF
3 0 obj
<</Length 49>>
stream
BT /F1 24 Tf 100 700 Td (Mene je nekdy vice)Tj ET
endstream
endobj
245 0 obj << /Type /Page /Parent 244 0 R /MediaBox [0 0 595 842] /Resources 2 0 R /Contents [3 0 R ] >>
endobj
xref
0 1
0000000000 65535 f
xref
3 1
0000033840 00000 n
xref
245 1
0000033937 00000 n
trailer
<</Size 245 /Root 243 0 R /Prev 28851>>
startxref
33938
%%EOF
```

---

<details><summary>FLAG:</summary>

```
flag{Alonzo_Church-6297}
```

</details>
