#### Challenge:

By following the information hidden in the text, R-Boy finds some very odd looking files in the directories. He can't understand what he's looking at and needs your help. [puzzle.zip.lzma](./puzzle.zip.lzma ":ignore")

---

#### Solution:

```bash
unzip -j ./puzzle.zip

for f in ./*; do
    if file ${f} | grep -q ASCII; then
        echo $(cat ${f} | tr ':' ' ') >> lookup.txt && rm $f
    fi
done

cat ./lookup.txt | awk '{print $3}' > cracked.txt # crack hashes

join -j 3 -o 1.1,1.2,1.3,2.4 <(sort -k 3 lookup.txt) <(sort -k 3 cracked.txt) | tr ' ' ':' > lookup-cracked.txt
while IFS= read -r l; do
    l=$(echo $l | tr -d '\r');
    test -e ${l%%:*} && 7z x ${l%%:*} -p${l##*:} && rm ${l%%:*};
done < lookup-cracked.txt

find . -type 'f' -size 718c -delete
```

```python
#!/usr/bin/env python3
from PIL import Image
import os

height = 0
width = 0

tuples = []
for root, dirnames, filenames in os.walk('./'):
    filenames = filter(lambda x: '.png' in x, filenames)
    filenames = sorted(filenames, key=lambda x: int(
        x.split('-')[1].split('.')[0]))

    for file in filenames:
        with Image.open(root + '/' + file) as slice:
            img = slice.load()
            height = slice.size[1]

            for w in range(slice.size[0]):
                collumn = []
                for h in range(height):
                    collumn.append(img[w, h])
                tuples.append(collumn)

            width += slice.size[0]


data = []
for h in range(height):
    for w in range(width):
        data.append(tuples[w][h])

with Image.new('RGB', (width, height)) as im:
    im.putdata(data)
    im.save('flag.png')
```

---

<details><summary>FLAG:</summary>

```
{FLG:ICOmpl3t3dMyPuzzl3!}
```

</details>
