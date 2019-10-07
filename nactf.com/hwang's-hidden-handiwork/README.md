#### Challenge:

Hwang was trying to hide secret photos from his parents. His mom found a text file with a secret string and an excel chart which she thinks could help you decrypt it. Can you help uncover Hwang's Handiwork?

Of course, the nobler of you may choose not to do this problem because you respect Hwang's privacy. That's ok, but you won't get the points. [hwangshandiwork.txt](./hwangshandiwork.txt ":ignore") [substitution.csv](./substitution.csv ":ignore")

---

#### Solution:

```python
#!/usr/bin/env python3

plaintext = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
             'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '/', '-', '_', '=', ':']
ciphertext = ['T', 'v', 'm', '9', 'M', 'j', '=', 'S', 'a', 'i', 'w', 'k', 'e', 'C', 'P', 'L', 'X', 'D', 'J', 'c', '8', 'h', 'f', '_', '.', 't', 'I', 'B', 'q', 'R', 'Q', 'Z', 'U',
              'n', 'K', 'u', 'l', 'E', '-', '7', '6', 'g', 'N', 'p', '/', 's', 'Y', '3', ':', '4', 'o', 'A', 'x', 'H', 'G', '1', 'b', 'F', 'W', '2', 'z', 'r', 'y', 'd', 'O', 'V', '5', '0']

decode_map = {}

for i in range(0, len(plaintext)):
    decode_map[ciphertext[i]] = plaintext[i]


def decode(payload):
    msg = ""
    for c in payload:
        if c in decode_map:
            msg += decode_map[c]
    return msg


print(decode('SccLJ0ddkSGy=PP=kM8JMDmPCcMCcymPedh9_r_GwDtt.::/.1TS_Ba:uU9KNpzir:VcNEVK/PPDXCImKlqK8rqtfOAvisA2MIikfjEq1ReFNC/gi_bf5fbrOSxrODf'))
```

- follow [link](https://lh3.googleusercontent.com/vdx0x3krzzyWWSy4ahxBiWJGdIQR9j0W_tQL_ISoorqnAcIKCIu0Czw-ZbjTZ8eAjlwfLC4Dm6QnSPjx5w)

---

<details><summary>FLAG:</summary>

```
nactf{g00gl3_15nt_s3cur3_3n0ugh}
```

</details>
