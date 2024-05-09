#### Challenge:

go with the [flow...](./enc ":ignore") [Source](./source.py ":ignore")

---

#### Solution:

We see the code using XOR encryption with some funky keystream generator. The problem with it is that it's seed is only `2 bytes` long. Armed with that knowledge and average consumer PC, I created code that will generate keystream rainbow table and then I brute-forced my way to the flag.

```python
import os
import zlib

def keystream(key):
    index = 0
    while 1:
        index+=1
        if index >= len(key):
            key += zlib.crc32(key).to_bytes(4,'big')
        yield key[index]

# read ciphertext
with open("enc","rb") as g:
    ciphertext = g.read()

# generate rainbowtable
rainbowtable=[]
for seed in range(255*255):
    k = keystream(seed.to_bytes(2,'big'))
    key = []
    
    for i in range(len(ciphertext)):
        key.append(next(k))

    rainbowtable.append(key)

# bruteforce
for row in rainbowtable:
    plaintext = ""
    for i in range(len(ciphertext)):
        plaintext += str(chr(ciphertext[i] ^ row[i])) 
    if "actf{" in plaintext:
        print(plaintext)
        break
```

---

<details><summary>FLAG:</summary>

```text
actf{low_entropy_keystream}
```

</details>
<br/>
