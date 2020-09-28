#### Challenge:

Decrypt the blinding lights. [nsW38Dh7Qx.zip](./nsW38Dh7Qx.zip ":ignore")

---

#### Solution:

Extracting the zip we see many `JPEG` files with same size containing white dots on black background. We quickly whip up script to merge them together. The resulting image shows flag in quite bad quality so it took some guesses until we figured the correct flag.

```python
from PIL import Image
from PIL import ImageChops
from PIL import ImageFilter
result = Image.open(f"nsW38Dh7Qx0.jpg").convert('1')
result.save('bw.png')
for i in range(299):
    print(i)
    im = Image.open(f"nsW38Dh7Qx{i}.jpg").convert('1')
    result = ImageChops.lighter(result, im)


result.show()
result.save('result.png')
```

---

<details><summary>FLAG:</summary>

```
Parsec{gla@d_y0u_d!dnt_f@!nt}
```

</details>
<br/>