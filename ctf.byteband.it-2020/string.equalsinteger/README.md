#### Challenge:

Someone gave me two functions to convert strings into integers. I converted some strings to the integers and noted them down. Can you help me converting the concatenation of those strings in the order mentioned in the file `hashes.txt` into integers?

The answer for this is the multiplication of output of both the functions for the concatenated string. (Wrap the number around flag{})

[hash.zip](./hash.zip ":ignore")

---

#### Solution:

- just bruteforce with lookup tables

```python
#!/usr/bin/python3

mod = int(1e9 + 7)
mod2 = int(1e9 + 9)


def func1(s):
    h = 0
    for i in range(len(s)):
        h += (ord(s[i]) - 96) * pow(31, i, mod)
        h %= mod
    return h


def func2(s):
    h = 0
    for i in range(len(s)):
        h += (ord(s[i]) - 96) * pow(31, i, mod2)
        h %= mod2
    return h


def func(s):
    h1 = 0
    h2 = 0
    hashes = []
    for i in range(len(s)):
        h1 += (ord(s[i]) - 96) * pow(31, i, mod)
        h2 += (ord(s[i]) - 96) * pow(31, i, mod2)
        h1 %= mod
        h2 %= mod2
        hashes.append(("%d %d" % (h1, h2), s[:i+1]))
    return hashes


lookup = {}
for i in range(20):
    with open("./hash/a/%d" % i) as f:
        content = f.read()
        for o in range(len(content)):
            for msg in func(content[o:o + 101]):
                lookup[msg[0]] = msg[1]

payload = ""
with open("./hash/hashes.txt", "r") as f:
    for l in f.readlines():
        payload += lookup[l.strip()]

print("flag{" + str(func1(payload) * func2(payload)) + "}")
```

---

<details><summary>FLAG:</summary>

```
flag{82806233047447860}
```

</details>
<br/>
