#### Challenge:

One of my logo designer left his job in the middle and hide my flag in it.Help me to get the flag. [stego1.xcf](./stego1.xcf ":ignore")

---

#### Solution:

```bash
echo -e `strings ./stego1.xcf | grep -i -A 2 'nothing here' | grep '(' | cut -d'"' -f 2` | xxd -r -p > data.bin
unzip -q data.zip
```

```python
from PIL import Image
from math import sqrt

tuples = []

with open('data.txt', 'r') as f:
    for line in f:
        for ch in line:
            if ch == '0':
                tuples.append((255, 255, 255))
            else:
                tuples.append((0, 0, 0))

img_size = int(sqrt(len(tuples)))
with Image.new('RGB', (img_size, img_size)) as im:
    im.putdata(tuples)
    im.save('data.png')
```

```bash
zbarimg ./data.png
```

---

<details><summary>FLAG:</summary>

```
d4rk{L0t5_0f_th1ng5_t0_d0_1n_th15_chAll@ng3}c0de
```

</details>