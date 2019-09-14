#### Challenge:

Nalezněte tajnou zprávu špiona-zelenáče. [50_odstinu_flagu.png.gz](./50_odstinu_flagu.png.gz ':ignore')

---

#### Solution:

```python
#!/usr/bin/env python3

from PIL import Image

tuples = []

with Image.open('50_odstinu_flagu.png', 'r') as img:
    for p in list(img.getdata()):
        if p[0] is 127:
            tuples.append((255, 255, 255))
        else:
            tuples.append((0, 0, 0))

    with Image.new('RGB', img.size) as im:
        im.putdata(tuples)
        im.save('flag.png')
```

---

<details><summary>FLAG:</summary>

```
flag{George_Boole-7064}
```

</details>
