#### Challenge:

Agent, we have intercepted an e-mail containing strange image (a line of black&white pixels) and a short text saying "The Smile of CESNET". Find the hidden message. Good luck, Agent [message.png](./message.png)

---

#### Solution:

```python
from PIL import Image

im = Image.open('message.png')
pix = im.load()

codes = []
byte = ""
for i in range(im.size[0]):
    if i % 7 == 0:
        byte = "0",
    if pix[i,0] == 0:
        byte += "1",
    else:
        byte += "0",
    if i % 7 == 6:
        codes.append(str(unichr(int("".join(byte),2))))
print "".join(codes)
```

---

<details><summary>FLAG:</summary>

```
CT18-BKuN-McWB-cBJR-QDXI
```

</details>
