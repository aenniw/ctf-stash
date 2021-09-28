#### Challenge:

Just a simple substitution cipher to get started... [substitution-cipher-i.sage](./substitution-cipher-i.sage ":ignore"), [output.txt](./output.txt ":ignore")

---

#### Solution:

- using the supplied `cipher` translation table can be build via encrypting `0123456789abcd...` printable characters

```python
e = [ ord(c) for c in '疗窇羑蒵觳轋钽驉鿯ꖯ𝻷𞣡🋥🴃𠜻𡆍𡯹𢙿𣄟𣯙𤚭𥆛𥲣𦟅𧌁𧹗𨧇𩕑𪃵𪲳𫢋𬑽𭂉𭲯𮣯𯕉㞷㬡㺥䉃䗻䧍䶹冿嗟娙幭招杣氅烁ꮉ녽랋붳쏵쩑탇𚖝𚻫𛡓𜇕𜭱𝔧𰆽𰹋𱫳흗玲𐃙𐠟𐽿𑛹𑺍𒘻𒸃𓗥𓷡𔗷𔸧𕙱𕻕𖝓𖿫𗢝𘅩𘩏𙍏𙱩']
d = [ c for c in '0123456789abcdefghijklmnopqrstuvwxyz!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}ACDEFGHIJKLMNOPQRSTUVWXYZ']

with open('./output.txt', 'r') as f:
    c = f.read(1)
    while c:
        try:
            print(d[e.index(ord(c))], end='')
        except:
            print(c, end='')
        c = f.read(1)
```

---

<details><summary>FLAG:</summary>

```
DUCTF{sh0uld'v3_us3d_r0t_13}
```

</details>
<br/>
