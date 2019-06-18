## Morse Code

Morse code is being used for a very long time. And since then there has been a lot of versions like using your eyebrows, flashing torches, tapping etc. [morse.txt](./morse.txt ':ignore')

```python
#!/usr/bin/env python3

# https://morsecode.scphillips.com/morse.html
table = {"di-dah": 'A',
         "dah-di-di-dit": 'B',
         "dah-di-dah-dit": 'C',
         "dah-di-dit": 'D',
         "dit": 'E',
         "di-di-dah-dit": 'F',
         "dah-dah-dit": 'G',
         "di-di-di-dit": 'H',
         "di-dit": 'I',
         "di-dah-dah-dah": 'J',
         "dah-di-dah": 'K',
         "di-dah-di-dit": 'L',
         "dah-dah": 'M',
         "dah-dit": 'N',
         "dah-dah-dah": 'O',
         "di-dah-dah-dit": 'P',
         "dah-dah-di-dah": 'Q',
         "di-dah-dit": 'R',
         "di-di-dit": 'S',
         "dah": 'T',
         "di-di-dah": 'U',
         "di-di-di-dah": 'V',
         "di-dah-dah": 'W',
         "dah-di-di-dah": 'X',
         "dah-di-dah-dah": 'Y',
         "dah-dah-di-dit": 'Z',
         "dah-dah-dah-dah-dah": '0',
         "di-dah-dah-dah-dah": '1',
         "di-di-dah-dah-dah": '2',
         "di-di-di-dah-dah": '3',
         "di-di-di-di-dah": '4',
         "di-di-di-di-dit": '5',
         "dah-di-di-di-dit": '6',
         "dah-dah-di-di-dit": '7',
         "dah-dah-dah-di-dit": '8',
         "dah-dah-dah-dah-dit": '9'}


with open('morse.txt') as fp:
    for cnt, line in enumerate(fp):
        for word in line.split(" "):
            if word in table:
                print(table[word], end='')
            else:
                print()

```

<details><summary>FLAG:</summary>

```
tryhackme{T3RN4TI0N4LM0RS3C0D}
```

</details>
