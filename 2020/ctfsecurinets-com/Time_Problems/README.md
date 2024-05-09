#### Challenge:

More magic on <a href="https://mega.nz/#!jKwygaTK!5lK2zxjvtbEqZLjgduCzTziyRfm6Y8boItf3BaFfbt8">this</a> one too :)

Author: bibiwars

---

#### Solution:

```bash
volatility -f for2.raw imageinfo
volatility -f for2.raw --profile=Win7SP1x86 pslist
git clone https://github.com/superponible/volatility-plugins.git
volatility --plugins=./volatility-plugins -f for2.raw --profile=Win7SP1x86 chromehistory | less
```

- visit http://52.205.164.112/ but it's down `Oups, Sorry mate, The flag is no longer available`
- try to check `WayBackMachine` https://web.archive.org/web/20200318121831/http://52.205.164.112/ -> `Securinets{█████_1s_my_f4vorit3_Pl4yer}`
- based on browse history try to add to blank space `neymar`/`Neymar`

---

<details><summary>FLAG:</summary>

```
Securinets{neymar_1s_my_f4vorit3_Pl4yer}
```

</details>
<br/>
