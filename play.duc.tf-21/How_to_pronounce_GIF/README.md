#### Challenge:

Our machine that makes QR Codes started playing up then it just said "PC LOAD LETTER" and died. This is all we could recover... [challenge.gif](./challenge.gif ":ignore")

---

#### Solution:

- extract the QR code frames from `gif`

```bash
convert -coalesce challenge.gif out-%05d.png
```

- stich the frames with the same color together

```python
from PIL import Image
import glob
import os

from PIL import Image

files = glob.glob("out-*.png")

qrs = {}
output = {}
for i in range(0, 10):
    qrs[str(i)] = []
    for infile in sorted(files):
        file, ext = os.path.splitext(infile)
        number = file.split("-")[1]
        if (int(number)+1) % 10 == i:
            qrs[str(i)].append(infile)

    new_image = Image.new('RGB', (300, 300))
    for k in range(len(qrs[str(i)])):
        img = Image.open(qrs[str(i)][k])
        new_image.paste(img, (0, k*(img.height - 1)))

    new_image.save(f'qr_{i}.png')

for f in files:
    os.remove(f)
```

- two QR codes contained `base64` segments, thus decode them and profit

```bash
echo -n $(zbarimg qr_6.png qr_8.png  | sed 's/.*://g') | tr -d ' '  | base64 -d
```

---

<details><summary>FLAG:</summary>

```
DUCTF{aM_1_haXX0r_n0w?}
```

</details>
<br/>
