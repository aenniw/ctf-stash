#### Challenge:

Prostě jen rozbalte archiv a přečtěte si obsah tajného souboru flag.txt. To by mělo být snadné, ne? [coze_jake_heslo.zip.gz](./coze_jake_heslo.zip.gz ':ignore')

---

#### Solution:

- fix dummy encrypted header based on https://users.cs.jmu.edu/buchhofp/forensics/formats/pkzip.html

```bash
hexedit ./coze_jake_heslo.zip
```

- fixed zip headers

```console
00000000   50 4B 03 04  14 00 08 00  08 00 00 00  21 00 00 00  00 00 00 00  00 00 15 00  00 00 08 00  14 00 66 6C  PK..........!.................fl
00000020   61 67 2E 74  78 74 55 54  01 00 00 75  78 0B 00 01  04 00 00 00  00 04 00 00  00 00 4B CB  49 4C AF 0E  ag.txtUT...ux.............K.IL..
00000040   2E 49 2D 4B  8D F7 CA 4F  2A D6 35 37  B6 30 AF 05  00 50 4B 07  08 D5 5C 94  FC 17 00 00  00 15 00 00  .I-K...O*.57.0...PK...\.........
00000060   00 50 4B 01  02 14 03 14  00 08 00 08  00 00 00 21  00 D5 5C 94  FC 17 00 00  00 15 00 00  00 08 00 14  .PK............!..\.............
00000080   00 00 00 00  00 00 00 00  00 A4 81 00  00 00 00 66  6C 61 67 2E  74 78 74 55  54 01 00 00  75 78 0B 00  ...............flag.txtUT...ux..
000000A0   01 04 00 00  00 00 04 00  00 00 00 50  4B 05 06 00  00 00 00 01  00 01 00 4A  00 00 00 61  00 00 00 00  ...........PK..........J...a....
000000C0   00
```

---

<details><summary>FLAG:</summary>

```
flag{Steve_Jobs-7387}
```

</details>
