#### Challenge:

Ah geez I lost my cat on the club penguin dance floor. Can you find her?

Creator: emalcxe!

[qr.png](./qr.png ":ignore")

---

#### Solution:

The provided image obviously contains some kind `QR code` but it is obfuscated by colors and it has `4 position segments` which is weird. Opening it in `Stegsolve` shows that there should be single valid `QR code` in each `R`, `G` and `B` channel just rotated by `90` resp. `180` degrees. The quality of it was not readable, so I made simple script that extracts the QR code(s) from the color channels and converts them to `BW` images, then simple QR scan gives the flag.

```python
#!/usr/bin/env python3

from PIL import Image, ImageOps

qr_red = Image.new(mode="RGB", size=(257, 252))
qr_green = Image.new(mode="RGB", size=(257, 252))
qr_blue = Image.new(mode="RGB", size=(257, 252))

with Image.open("qr.png", 'r') as qr_orig:
    pix = qr_orig.load()
    pix_red = qr_red.load()
    pix_green = qr_green.load()
    pix_blue = qr_blue.load()

    for y in range(0,252):
        for x in range(0,257):
            pix_red[x, y] = (pix[x, y][0], pix[x, y][0], pix[x, y][0])
            pix_green[x, y] = (pix[x, y][1], pix[x, y][1], pix[x, y][1])
            pix_blue[x, y] = (pix[x, y][2], pix[x, y][2], pix[x, y][2])


qr_red = ImageOps.invert(qr_red)
qr_red = qr_red.convert('L')
qr_red = qr_red.point( lambda p: 255 if p >250  else 0 )
qr_red = qr_red.convert('1')
qr_red.save("qr_red.png")
qr_red.show()


qr_green = ImageOps.invert(qr_green)
qr_green = qr_green.convert('L')
qr_green = qr_green.point( lambda p: 255 if p >250  else 0 )
qr_green = qr_green.convert('1')
qr_green.save("qr_green.png")
qr_green.show()


qr_blue = ImageOps.invert(qr_blue)
qr_blue = qr_blue.convert('L')
qr_blue = qr_blue.point( lambda p: 255 if p >250  else 0 )
qr_blue = qr_blue.convert('1')
qr_blue.save("qr_blue.png")
qr_blue.show()
```

---

<details><summary>FLAG:</summary>

```
WPI{KITTYCATQRCODE}
```

</details>
<br/>
