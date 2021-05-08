#### Challenge:

Baby's first reversing, I think. Get it to terminate with exit 0 with an input matching the flag format (WPI{foo bar baz})

[mhm](./mhm ":ignore")

---

#### Solution:

We are given what seems to be Python byte-compiled code (`PYC` file). Using [decompyle3](https://github.com/rocky/python-decompile3) tool I was able to decompile it and modify it to print the flag:

```bash
cp mhm mhm.pyc
python3 decompyle3 mhm.pyc
```

```python
def __main__():
    for i in range(-4,11):
        if i == 4:
            print(' ', end="")
        if i == -4:
            print('W', end="")
        if i == -2:
            print('I', end="")
        if i == -1:
            print('{', end="")
        if i == 10:
            print('}', end="")
        if i == 1:
            print('@', end="")
        if i == 2:
            print('5', end="")
        if i == 7:
            print('P', end="")
        if i == 3:
            print('E', end="")
        if i == 0:
            print('h', end="")
        if i == 5:
            print('h', end="")
        if i == -3:
            print('P', end="")
        if i == 9:
            print('!', end="")
        if i == 6:
            print('0', end="")
        if i == 8:
            print('3', end="")
        i += 1
    else:
        print(':)')

__main__()
```

---

<details><summary>FLAG:</summary>

```
WPI{h@5E h0P3!}
```

</details>
<br/>
