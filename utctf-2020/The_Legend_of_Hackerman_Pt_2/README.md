#### Challenge:

Ok, I've received another file from Hackerman, but it's just a Word Document? He said that he attached a picture of the flag, but I can't find it...
[Hacker.docx](./Hacker.docx ":ignore")

---

#### Solution:

```bash
binwalk -Me ./Hacker.docx
eog _Hacker.docx.extracted/word/media/image23.png
```

---

<details><summary>FLAG:</summary>

```
utflag{unz1p_3v3ryth1ng}
```

</details>
<br/>
