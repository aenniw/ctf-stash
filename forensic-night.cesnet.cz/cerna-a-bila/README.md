#### Challenge:

CESNET ve svém logu místo černé používá raději #0068A2, ale to je skoro stejné. [black_and_white.png.gz](./black_and_white.png.gz ":ignore")

---

#### Solution:

```python
#!/usr/bin/env python3

from PIL import Image

codes = []
byte = ""

with Image.open('black_and_white.png', 'r') as img:
    pix = img.load()
    for i in range(img.size[0]):
        if i % 7 == 0:
            byte = "0",
        if pix[i, 0] == 0:
            byte += "1",
        else:
            byte += "0",
        if i % 7 == 6:
            codes.append(str(chr(int("".join(byte), 2))))
print("".join(codes))
```

---

<details><summary>FLAG:</summary>

```
flag{Matthew_Mullenweg-0371}
```

</details>
