#### Challenge:

More magic on <a href="https://mega.nz/#!jKwygaTK!5lK2zxjvtbEqZLjgduCzTziyRfm6Y8boItf3BaFfbt8">this</a> one too :)

Author: bibiwars

---

#### Solution:

```bash
volatility -f ./for2.raw imageinfo
volatility -f for2.raw --profile=Win7SP1x86 pslist
mkdir plugins && cd plugins
wget https://raw.githubusercontent.com/superponible/volatility-plugins/master/chromehistory.py
wget https://raw.githubusercontent.com/superponible/volatility-plugins/master/sqlite_help.py
cd -
volatility --plugins=./plugins/ chromehistory -f for2.raw --profile=Win7SP1x86 | less
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
