## LSB

Hiding data in LSB are a very common process. Especially in CTFs.
The most famous tool used for this is KDE68
P.S: Name of the tool is encrypted in a version of ROT cipher.
P.P.S: I repeat decode KDE68 to find the name of the tool. [stegano.png](./stegano.png ':ignore')

[CyberChef](<https://gchq.github.io/CyberChef/#recipe=ROT47(15)&input=S0RFNjg>)

```bash
gem install zsteg
zsteg ./stegano.png | grep flag
```

[CyberChef](https://gchq.github.io/CyberChef/)
```json
[
  {
    "op": "From Base58",
    "args": [
      "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz",
      false
    ]
  },
  { "op": "From Base32", "args": ["A-Z2-7=", false] }
]
```

<details><summary>FLAG:</summary>

```
tryhackme{lsb_4r3_l1t!!}
```

</details>
