#### Challenge:

Hi Commander,

although we can now decode the standard messages, the Berserkers use some kind of encryption based on images and equations to secure messages of high importance. We have intercept, acquired and decoded first layer of such message - it has been broadcasted by a berserker called `A.Einstein`. The message consists just of two images. According to data from our improved infiltrators (they get new stickers `Nuke the badlives!`) the encryption is symetric one and the key to the solution should be some equation.

Good luck! [message.tar.gz](./message.tar.gz ":ignore")

---

#### Solution:

```python
#!/usr/bin/env python3

from PIL import Image


def hex_to_rgb(hex):
    hex = hex.split('0x')[1]
    return (0, 0, int(hex[-2:], 16))


with Image.open('m.png') as m_png:
    with Image.open('c.png') as c_png:
        m = m_png.load()
        c = c_png.load()

        tuples = []
        for o in range(m_png.size[1]):
            for i in range(m_png.size[0]):
                color = "{0:#0{1}x}".format(
                    int(m[i, o] * c[i, o] * c[i, o]), 8)
                tuples.append(hex_to_rgb(color))

        with Image.new('RGB', m_png.size) as im:
            im.putdata(tuples)
            im.save('flag.png')
```

---

<details><summary>FLAG:</summary>

```
FLAG{zLjD-Rn5c-et97-yukm}
```

</details>
