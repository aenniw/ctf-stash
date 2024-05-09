#### Challenge:

Hi, packet inspector,

the AI has "upgraded" our packet auditing system &ndash; time to time, it generates archive of pictures, where the state of packet and the appropriate delivery team is indicated by different colours for each packet transport number.

We have a plea from `Brenda's delivery team` to find their missing packet in state `ready for pickup` (the other teams have already delivered all their packages mentioned in last given audit archive).

 Download [audit archive](https://owncloud.cesnet.cz/index.php/s/BGSbaBDCsuWdAYO) (MD5 checksum `08ee155d2c9aee13ea5cab0a11196129`), find the desired pickup code and enter it on webpage [http://pickup.mysterious-delivery.thecatch.cz](http://pickup.mysterious-delivery.thecatch.cz) to collect pickup code.

May the Packet be with you!

---

#### Solution:

- all the packages have color coding based on their state and team, all that we need to do, is to check all the available images and check the color of the package and team background. This is pretty simple, as all the images are generated from the same template, so we need to check just 2 pixels for each image, that we specifically select.

```python
from PIL import Image

def check(file):
    with Image.open(file, 'r') as img:
        pixels = img.load()
        backgound = pixels[img.size[0]/2, 0]
        package = pixels[img.size[0]/10,img.size[1]/2]

        if backgound[0] > backgound[1] and backgound[0] > backgound[2] and backgound[0] > 200\
            and package[1] > package[0] and package[1] > package[2]:
            print(file, backgound)

from pathlib import Path

pathlist = Path("./").glob('**/*.png')
for path in pathlist:
     path_in_str = str(path)
     if path_in_str.endswith('.png'):
        check(path_in_str)
```

- after looking up the code we can retrieve the flag from delivery portal

---

<details><summary>FLAG:</summary>

```
FLAG{rNM8-Aa5G-dF5y-6LqY}
```

</details>
<br/>
