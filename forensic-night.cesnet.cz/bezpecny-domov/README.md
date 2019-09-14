#### Challenge:

Přístupový kód do chytrého domu (smart-bio-eko-house) je ověřován v přilloženém programu. Zjistěte, zda návrhář neudělal nějakou chybu, která umožní kód získat. [validator.vbs.gz](./validator.vbs.gz ':ignore')

---

#### Solution:

```console
(Hex(Asc(Mid(DDVV, 1, 1))) <> "50")                         => chr(int('0x50', 16))     => 'P'
(Asc(Mid(DDVV, 2, 1)) <> 97)                                => chr(97)                  => 'a'
(Asc(Mid(DDVV, 3, 1)) <> 118)                               => chr(118)                 => 'v'
(Hex(Asc(Mid(DDVV, 4, 1))) <> "65")                         => chr(int('0x65', 16))     => 'e'
(Asc(Mid(DDVV, 5, 1)) <> 108)                               => chr(108)                 => 'l'
(Oct(Asc(Mid(DDVV, 6, 1))) <> 137)                          => chr(int('137', 8))       => '_'
(Oct(Asc(Mid(DDVV, 7, 1))) <> 110)                          => chr(int('110', 8))       => 'H'
((Asc(Mid(DDVV, 8, 1)) - Asc(Mid(DDVV, 7, 1))) <> 29)       => chr(29 + ord('H'))       => 'e'
(Oct(Asc(Mid(DDVV, 9, 1))) <> 162)                          => chr(int('162', 8))       => 'r'
(Oct(Asc(Mid(DDVV, 10, 1))) <> 157)                         => chr(int('157', 8))       => 'o'
((Asc(Mid(DDVV, 11, 1)) - Asc(Mid(DDVV, 10, 1))) <> 6)      => chr(6 + ord('o'))        => 'u'
(Oct(Asc(Mid(DDVV, 12, 1))) <> 164)                         => chr(int('164', 8))       => 't'
(Mid(DDVV, 13, 1) <> "-")                                   =>                          => '-'
(Asc(Mid(DDVV, 14, 1)) <> 56)                               => chr(56)                  => '8'
((Asc(Mid(DDVV, 15, 1)) - Asc(Mid(DDVV, 14, 1))) <> -4)     => chr(-4 + ord('8'))       => '4'
(Mid(DDVV, 16, 1) <> "0")                                   =>                          => '0'
(Oct(Asc(Mid(DDVV, 17, 1))) <> 62)                          => chr(int('62', 8))        => '2'
```

---

<details><summary>FLAG:</summary>

```
flag{Pavel_Herout-8402}
```

</details>
