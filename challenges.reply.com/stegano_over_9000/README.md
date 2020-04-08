#### Challenge:

Oh boy! It's clear Armstrong's been kidnapped. According to the clues, he was snatched by some kind of robotic human-hating aliens with a passion for weird internet memes. R-boy discovers a website that probably contains more useful information for rescuing Armstrong. However, it seems to be protected by some anti-human access mechanism. Can you bypass it?

---

#### Solution:

The target site is captcha protected. But the captcha pictures look like green-blue noise. After opening one of the captcha images in `stegsolve` we found `linear equation` in the `green plane` and a weird black line in `blue plane`. After closer observation, we noticed that the line corresponds to the coordinates given by the linear equation and also that the line is not entirely black (`0` in blue plane) from the start to end, but has some different values in it's beginning. Automating the equation extraction with `OCR` and dumping the values of the line in `python`, we get values that can be represented as `ASCII characters`. After using these as the captcha code 5 times, we get to site containing 5 fully `url-encoded` links. Four of the links lead to different memes (discarding the session and forcing you to go through captcha again) and the fifth leads to page with the flag.

```python
#!/bin/env python3
# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup as BS
from PIL import Image
import requests
from urllib.request import urlretrieve
import parser
import math

import pytesseract
pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

ses = requests.session()
page = ses.get('http://gamebox1.reply.it/ae6cdb9098e1252ec193b2c50587d1b3/')

## We need to solve 5 captchas
for step in range(5):

    ## Get the captcha image from the site
    beautiful_soup = BS(page.content, 'html.parser')
    for img_tag in beautiful_soup.find_all('img'):
        img64 = img_tag['src']

    filename, m = urlretrieve(img64)
    original_image = Image.open(filename)
    original_image_pixels = original_image.load()

    ## Extract the equation for the line from green LSB
    green_image = Image.new('RGB', (original_image.size[0],original_image.size[1]),"white")
    green_pixels = green_image.load()

    for y in range(original_image.size[1]):
        for x in range(original_image.size[0]):
            green_lsb = int((original_image_pixels[x,y][1]&0b00000001)<<8)
            green_pixels[x,y] = (green_lsb,green_lsb,green_lsb)

    formula = pytesseract.image_to_string(green_image)
    print(formula)

    equation = parser.expr(formula[10:].replace("x", "*x")).compile()

    ## Extract the captcha from the line defined by equation in blue channel
    blue_image = Image.new('RGB', (original_image.size[0],original_image.size[1]),"white")
    blue_image_pixels = blue_image.load()

    captcha = ""
    for x in range(original_image.size[0]):
        y = math.floor(eval(equation))
        if original_image_pixels[x, y][2] != 0:
            captcha = captcha + chr(original_image_pixels[x, y][2])
            print(x, "x", y, " = ",  chr(original_image_pixels[x, y][2]))
        blue_image_pixels[x, y] = ((original_image_pixels[x, y][0]),(original_image_pixels[x, y][1]),(original_image_pixels[x, y][2]))

    ## Send the captcha
    page = ses.post('http://gamebox1.reply.it/ae6cdb9098e1252ec193b2c50587d1b3/', data={'response':captcha})
    text_response = page.text
    print(text_response)

    f = open("response_"+step+".html","w+")
    f.write(text_response)

## Write out the final response page
## This is actually the page that the correct link of the 5 leads to.
page = ses.get('http://gamebox1.reply.it/ae6cdb9098e1252ec193b2c50587d1b3/58f5c08dd0131e49275cd553a9063131')
text_response = page.text
print(text_response)

f = open("final_response.html", "w+")
f.write(text_response)
```

---

<details><summary>FLAG:</summary>

```
{FLG:Oh_M4m4m14_M4m4m14_L3tM3Go}
```

</details>
