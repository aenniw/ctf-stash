#### Challenge:

Hi Commander,

although we can now decode the standard messages, the Berserkers use some kind of encryption based on images and equations to secure messages of high importance. We have intercept, acquired and decoded first layer of such message - it has been broadcasted by a berserker called `A.Einstein`. The message consists just of two images. According to data from our improved infiltrators (they get new stickers `Nuke the badlives!`) the encryption is symetric one and the key to the solution should be some equation.

Good luck! [message.tar.gz](./message.tar.gz ":ignore")

---

#### Solution:

```python
#!/usr/bin/env python3

from PIL import Image

c = Image.open("c.png")
c_pix = c.load()

m = Image.open("m.png")
m_pix = m.load()

e = Image.new('L',(c.size[0],c.size[1]))
e_pix = e.load()

for o in range(c.size[1]):
    for i in range(c.size[0]):

        # Because A. Einstein is the hint:
        # e = mc^2   // 24 bit number
        mcc = (m_pix[i, o] * c_pix[i, o] * c_pix[i, o])

        # Take only 8 Least Significant Bits
        e_pix[i,o] = ((mcc & 0xFF))

e.save('e.png',"PNG")
e.show()
```

---

<details><summary>FLAG:</summary>

```
FLAG{zLjD-Rn5c-et97-yukm}
```

</details>
