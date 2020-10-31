#### Challenge:

At first, R-Boy discovers the ‘limbo zone’ where, caught in a trap, he meets Virgilia, a guide and protector of the temporal dimension. Virgilia has probably been trapped by Zer0, but R-Boy can release her by decrypting the code.

---

#### Solution:

We are presented with `level_0.7z` archive containing another archive `level_1.7z` (encrypted with password), two images `level_0.png` and `lev3l_0.png` which seem to be differing only in one pixel and a python script `ForceLevel.py`, which shows how to construct password to the encrypted zip while brute forcing the pixels of the provided images. Writing a heuristic by comparing the images unlocks the archive and provide us with another level of the same problem. In some later levels the images need to be adjusted by different operations to yeld the pixel needed to construct password.

For the purposes of saving space and time, this repository contains only the archive [level_1024.7z](./level_1024.7z ":ignore") and the images [level_1023.png](./level_1023.png ":ignore"), [lev3l_1023.png](./lev3l_1023.png ":ignore") with the last level. The solution script was updated accordingly. If you wish to run it on [original archive](https://challenges.reply.com/tamtamy/file/download-332768.action) from level 0, use the for-loop for all levels and uncomment the block responsible for deleting intermediary levels, otherwise solving full extent of this task can easily fill up your disk!

```python
#!/usr/bin/env python3

import os
import py7zr
from PIL import Image, ImageChops, ImageOps

def count_nonblack_pil(img):
    """Return the number of pixels in img that are not black.
    img must be a PIL.Image object in mode RGB.

    """
    bbox = img.getbbox()
    if not bbox: return 0
    return sum(img.crop(bbox)
               .point(lambda x: 255 if x else 0)
               .convert("L")
               .point(bool)
               .getdata())

def tryOpen(password, level):
    try:
        with py7zr.SevenZipFile('level_'+str(level)+'.7z', mode='r', password=password) as z:
            z.extractall()
    except:
        print("wrong pass")
        exit(0)


def main():
    # for level in range(0,1024): # for loop for all levels
    for level in range(1023,1024): # for loop for last level
        print("level:"+str(level))
        with Image.open('level_'+str(level)+'.png', 'r') as img1:
            with Image.open('lev3l_'+str(level)+'.png', 'r') as img2:

                difference = ImageChops.difference(img1, img2)

                ## Check the difference for debug purposes - to see if the images really differ in only one pixel
                # difference.save("difference.png")

                diff_pix_count=count_nonblack_pil(difference)

                if diff_pix_count>1:
                    for op in [Image.FLIP_LEFT_RIGHT, Image.FLIP_TOP_BOTTOM, Image.ROTATE_180, Image.ROTATE_270, Image.TRANSPOSE, Image.TRANSVERSE, Image.ROTATE_90]:
                        newimg2 = img2.transpose(op)
                        difference = ImageChops.difference(img1, newimg2)

                        ## Check the difference for debug purposes - to see if the images really differ in only one pixel
                        # difference.save("difference"+str(op)+".png")

                        diff_pix_count=count_nonblack_pil(difference)

                        if diff_pix_count==1:
                            img2 = newimg2
                            break;

                pix1 = img1.load()
                pix2 = img2.load()
                for x in range(img1.size[0]):
                    for y in range(img1.size[1]):
                        r1 = pix1[x, y][(0)]
                        g1 = pix1[x, y][(1)]
                        b1 = pix1[x, y][(2)]

                        r2 = pix2[x, y][(0)]
                        g2 = pix2[x, y][(1)]
                        b2 = pix2[x, y][(2)]

                        if r1 == r2 and g1 == g2 and b1 == b2:
                            continue

                        xy = str(x) + str(y)
                        rgb1 = '{:0{}X}'.format(r1, 2) + '{:0{}X}'.format(g1, 2) + '{:0{}X}'.format(b1, 2)
                        rgb2 = '{:0{}X}'.format(r2, 2) + '{:0{}X}'.format(g2, 2) + '{:0{}X}'.format(b2, 2)
                        print("trying: "+xy + rgb1 + rgb2)
                        tryOpen(xy + rgb1 + rgb2, level+1)

                        ## Block for deleting intermediary levels

                        # if level > 1:
                        #     os.remove("lev3l_"+str(level-1)+".png")
                        #     os.remove("level_"+str(level-1)+".png")
                        #     os.remove("level_"+str(level)+".7z")

if __name__ == "__main__":
    main()
```

---

<details><summary>FLAG:</summary>

```
{FLG:p1xel0ut0fBound3xcept1on_tr4p_1s_shutt1ng_d0wn}
```

</details>
