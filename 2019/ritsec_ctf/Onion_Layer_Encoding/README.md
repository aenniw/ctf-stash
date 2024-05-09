#### Challenge:

Encoding is not encryption, but what if I just encode the flag with base16,32,64?
If I encode my precious flag for 150 times, surely no one will be able to decode it, right? [onionlayerencoding.txt.tar.lzma](./onionlayerencoding.txt.tar.lzma ":ignore")

---

#### Solution:

```bash
tar --lzma -xvf onionlayerencoding.txt.tar.lzma
```

```python
#!/usr/bin/python3

import base64


def decode(data):
    result = ""
    try:
        print("b16")
        result = base64.b16decode(data)
    except:
        pass
    if len(result) > 0 and '\\x' not in str(result):
        return result
    try:
        print("b32")
        result = base64.b32decode(data)
    except:
        pass
    if len(result) > 0 and '\\x' not in str(result):
        return result
    try:
        print("b64")
        result = base64.b64decode(data)
    except:
        pass
    if len(result) > 0 and '\\x' not in str(result):
        return result
    print(data)
    exit(0)


with open('onionlayerencoding.txt', 'r') as file:
    data = file.read()
    for i in range(150):
        data = decode(data)

```

---

<details><summary>FLAG:</summary>

```
RITSEC{0n1On_L4y3R}
```

</details>
<br/>
