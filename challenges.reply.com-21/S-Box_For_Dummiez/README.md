#### Challenge:

Reunited at the Temple of Nebula, the Five Legends and R-Boy prepare their final attack. [misc100-readme.pdf](./misc100-readme.pdf ":ignore")

---

#### Solution:

```python
mem = 'a_cdefaijkltmnopwzstueabez01200067890ABCDEFGHIJKnooodtdvw000eta?T!VW00Y!ETA?*-+/{}[]=&%£"!()abcdefghijklmnopqrsABCDEFGHIJKLNMuuuvwxipsilonnnnnnz%%/9876543210|!"£$ohdear!%&/(((()*;:_AAAABSIDEOWabcdefghijklmnopqrstuvwxyz012345678?8?8?8?9!!!!!EGIN.CERTIFICATEa_cdefaijkltmnopwzstueabez01200067890ABCDEFGHIJKnooodtdvw000eta?T!VW00Y!ETA?*-+/{}[]=&%£"!()abcdefghijklmnopqrsABCDEFGHIJKLNMuuuvwxipsilonnnnnnz%%/9876543210|!"£$ohdear!%&/(((()*;:_AAAABSIDEOWabcdefghijklmnopqrstuvwxyz012345678?8?8?8?9!!!!!EGIN.CERTIFICATE'


def ADD(i):
    table = {
        '000': [0, 0],
        '001': [0, 1],
        '010': [0, 1],
        '011': [1, 0],
        '100': [0, 1],
        '101': [1, 0],
        '110': [1, 0],
        '111': [1, 1]
    }
    return table[''.join([str(c) for c in i])]


def NOT(v):
    return 0 if v else 1


def circuit(i):
    o = [
        0,
        i[5],
        ADD([i[3], i[4], i[2]])[0] ^ i[6],
        ADD([i[3], i[4], i[2]])[1],
        0,
        i[0],
        i[5] ^ i[0],
        i[7] & i[1],
        0,
    ]
    o[0] = i[8] ^ o[2]
    o[8] = i[8] ^ o[6]
    o[4] = o[3] or i[0] or NOT(i[5])

    return o


def step(s):
    s = circuit(s)
    a = int(''.join([str(c) for c in s])[::-1], 2)
    print(mem[a], end='')
    return s


print('{FLG:', end='')
s = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(0, 0xa):
    s = step(s)
print('}')
```

---

<details><summary>FLAG:</summary>

```
{FLG:weeGo0dY0u}
```

</details>
