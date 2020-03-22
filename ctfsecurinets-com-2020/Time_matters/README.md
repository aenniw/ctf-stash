#### Challenge:

Just do some magic on this <a href="https://mega.nz/#!3ehmRQLB!pQBPFR415KeXX2N8tvrwOFupYzzfdkSbp2v-DsNaq40">file</a>

---

#### Solution:

```bash
volatility -f ./for1.raw imageinfo
volatility -f for1.raw --profile=Win7SP1x86 filescan
#   0x000000001e24bcd0      2      1 R--rwd \Device\HarddiskVolume2\Users\studio\Desktop\steghide
#   0x000000001e45e730      8      0 R--rwd \Device\HarddiskVolume2\Users\studio\Desktop\DS0394.jpg
volatility -f for1.raw --profile=Win7SP1x86 dumpfiles -Q 0x000000001e45e730 -n -D ./

mkdir plugins && cd plugins
wget https://raw.githubusercontent.com/dfirfpi/hotoloti/master/volatility/mimikatz.py
cd -
volatility --plugins=./ mimikatz -f for1.raw --profile=Win7SP1x86
#   wdigest  studio           studio-PC        Messi2020
```

- password `Messi2020` doesn't works, so based on timestamp in img try `Messi2019`

```bash
steghide extract -sf file.None.0x85f45558.DS0394.jpg.dat -p Messi2019
```

---

<details><summary>FLAG:</summary>

```
Securinets{c7e2723752111ed983249627a3d752d6}
```

</details>
<br/>
