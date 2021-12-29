#### Challenge:

Hi Expert,

oh no, bad news! All archaeologist computers connected to discovered port were infected by some kind of self-changing malware - it changes its file name and also its hash differs (i.e. the content change) after each run. Find the algorithm of name change in order to get some IoC (Indicators of Compromise). Download the file [`nomen-omen.zip`](./nomen-omen.zip ":ignore") (password for archive: `infected`).

Good Luck!

---

#### Solution:

```powershell
$Env:APPDATA="$pwd\"

for (($i = 0); $i -lt 1000; $i++) { 
    Get-ChildItem -recurse | Sort-Object -Descending LastWriteTime | select -First 1 | ForEach-Object {& $_.FullName} 
}
ls flag*
```

---

<details><summary>FLAG:</summary>

```
flag{fwsg-iboz-hmlt-pqhz}
```

</details>
<br/>
