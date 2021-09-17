#### Challenge:

What's up with all the zeros and ones? Where are my letters and numbers? (This is a reversing challenge.) [checker.py](./checker.py ":ignore")

---

#### Solution:

- reversing provided operations decodes the flag

```python
#!/bin/python3

def down(x):
    x = ''.join(['1' if x[i] == '0' else '0' for i in range(len(x))])
    return x

def left(x,d):
    x = right(x,len(x)-d)
    return x[::-1]

def right(x,d):
    x = x[d:] + x[0:d]
    return x

def decode(x):
    d = 24
    x = left(x,d)
    x = down(x)
    x = un_right(x,d)
    x = un_up(x)
    return x

def un_up(x):
    d = []
    for i in range(0,len(x), 8):
        d.append(chr(int(x[i: i+8], 2) >> 1))
    return ''.join(d)

def un_right(x,d):
    d = len(x) - d
    x = x[d:] + x[0:d]
    return x


print(decode(
    "1010000011111000101010101000001010100100110110001111111010001000100000101000111011000100101111011001100011011000101011001100100010011001110110001001000010001100101111001110010011001100"
))
```

---

<details><summary>FLAG:</summary>

```
flag{r3vers!nG_w@rm_Up}
```

</details>
<br/>
