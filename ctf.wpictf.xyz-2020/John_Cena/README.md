#### Challenge:

You can't see him, but can you see the flag?

[braille.png](./braille.png ":ignore")

---

#### Solution:

```python
#!/usr/bin/env python3
from PIL import Image

payload = ""


def decodeRow(row=[]):
    global payload
    colLen = len(row[0])

    for co in range(8, colLen - 15, 15):
        black = 0
        other = 0
        for c in range(15):
            for r in range(len(row)):
                if row[r][c + co] == (0, 0, 0, 255):
                    black += 1
                else:
                    other += 1

        if black > other:
            payload += '0'
        else:
            payload += '1'
    payload += '\n'


with Image.open("braille.png") as braile:
    img = braile.load()

    pixels = []
    for r in range(braile.size[1]):
        allBlackRow = True
        for c in range(braile.size[0]):
            allBlackRow = allBlackRow and img[(c, r)] == (0, 0, 0, 255)
            if not allBlackRow:
                break
        if allBlackRow:
            if len(pixels) > 0:
                decodeRow(pixels)
            pixels = []
            continue

        row = []
        for c in range(braile.size[0]):
            row.append(img[c, r])
        pixels.append(row)


brailles = ['⠀', '⠮', '⠐', '⠼', '⠫', '⠩', '⠯', '⠄', '⠷', '⠾', '⠡', '⠬', '⠠', '⠤', '⠨', '⠌', '⠴', '⠂', '⠆', '⠒', '⠲', '⠢',
            '⠖', '⠶', '⠦', '⠔', '⠱', '⠰', '⠣', '⠿', '⠜', '⠹', '⠈', '⠁', '⠃', '⠉', '⠙', '⠑', '⠋', '⠛', '⠓', '⠊', '⠚', '⠅',
            '⠇', '⠍', '⠝', '⠕', '⠏', '⠟', '⠗', '⠎', '⠞', '⠥', '⠧', '⠺', '⠭', '⠽', '⠵', '⠪', '⠳', '⠻', '⠘', '⠸']

matrixcodes = [
    [[0, 0], [0, 0], [0, 0]], [[0, 1], [1, 0], [1, 1]], [
        [0, 0], [0, 1], [0, 0]], [[0, 1], [0, 1], [1, 1]],
    [[1, 1], [1, 0], [0, 1]], [[1, 1], [0, 0], [0, 1]], [
        [1, 1], [1, 0], [1, 1]], [[0, 0], [0, 0], [1, 0]],
    [[1, 0], [1, 1], [1, 1]], [[0, 1], [1, 1], [1, 1]], [
        [1, 0], [0, 0], [0, 1]], [[0, 1], [0, 0], [1, 1]],
    [[0, 0], [0, 0], [0, 1]], [[0, 0], [0, 0], [1, 1]], [
        [0, 1], [0, 0], [0, 1]], [[0, 1], [0, 0], [1, 0]],
    [[0, 0], [0, 1], [1, 1]], [[0, 0], [1, 0], [0, 0]], [
        [0, 0], [1, 0], [1, 0]], [[0, 0], [1, 1], [0, 0]],
    [[0, 0], [1, 1], [0, 1]], [[0, 0], [1, 0], [0, 1]], [
        [0, 0], [1, 1], [1, 0]], [[0, 0], [1, 1], [1, 1]],
    [[0, 0], [1, 0], [1, 1]], [[0, 0], [0, 1], [1, 0]], [
        [1, 0], [0, 1], [0, 1]], [[0, 0], [0, 1], [0, 1]],
    [[1, 0], [1, 0], [0, 1]], [[1, 1], [1, 1], [1, 1]], [
        [0, 1], [0, 1], [1, 0]], [[1, 1], [0, 1], [0, 1]],
    [[0, 1], [0, 0], [0, 0]], [[1, 0], [0, 0], [0, 0]], [
        [1, 0], [1, 0], [0, 0]], [[1, 1], [0, 0], [0, 0]],
    [[1, 1], [0, 1], [0, 0]], [[1, 0], [0, 1], [0, 0]], [
        [1, 1], [1, 0], [0, 0]], [[1, 1], [1, 1], [0, 0]],
    [[1, 0], [1, 1], [0, 0]], [[0, 1], [1, 0], [0, 0]], [
        [0, 1], [1, 1], [0, 0]], [[1, 0], [0, 0], [1, 0]],
    [[1, 0], [1, 0], [1, 0]], [[1, 1], [0, 0], [1, 0]], [
        [1, 1], [0, 1], [1, 0]], [[1, 0], [0, 1], [1, 0]],
    [[1, 1], [1, 0], [1, 0]], [[1, 1], [1, 1], [1, 0]], [
        [1, 0], [1, 1], [1, 0]], [[0, 1], [1, 0], [1, 0]],
    [[0, 1], [1, 1], [1, 0]], [[1, 0], [0, 0], [1, 1]], [
        [1, 0], [1, 0], [1, 1]], [[0, 1], [1, 1], [0, 1]],
    [[1, 1], [0, 0], [1, 1]], [[1, 1], [0, 1], [1, 1]], [
        [1, 0], [0, 1], [1, 1]], [[0, 1], [1, 0], [0, 1]],
    [[1, 0], [1, 1], [0, 1]], [[1, 1], [1, 1], [0, 1]], [
        [0, 1], [0, 1], [0, 0]], [[0, 1], [0, 1], [0, 1]]
]

lines = payload.splitlines()
payload = ''
for o in range(0, len(lines)-1, 3):
    line1 = lines[o]
    line2 = lines[o+1]
    line3 = lines[o+2]
    for i in range(0, len(line1), 2):
        key = [[int(line1[i]), int(line1[i+1])],
               [int(line2[i]), int(line2[i+1])],
               [int(line3[i]), int(line3[i+1])]]
        payload += brailles[matrixcodes.index(key)]

print(payload)
```

- decode `UTF` braille characters with https://cable.ayra.ch/braille/
- decode hex values [CyberChef - From hex](<https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')&input=N2Y0NTRjNDYwMjAxMDEwMDAwMDAwMDAwMDAwMDAwMDAwMjAwM2UwMDAxMDAwMDAwODAwMDQwMDAwMDAwMDAwMDQwMDAwMDAwMDAwMDAwMDBlMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDA0MDAwMzgwMDAxMDA0MDAwMDQwMDAzMDAwMTAwMDAwMDA3MDAwMDAwODAwMDAwMDAwMDAwMDAwMDgwMDA0MDAwMDAwMDAwMDA4MDAwNDAwMDAwMDAwMDAwNDkwMDAwMDAwMDAwMDAwMDQ5MDAwMDAwMDAwMDAwMDAxMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMGI4MDEwMDAwMDBiZjAxMDAwMDAwYmViNDAwNDAwMDMxYzk2NzhiMTQwZTgzYzIzMTY3ODkxNDBlZmZjMTgzZjkxNTc1ZWViYTE1MDAwMDAwMGYwNWI4M2MwMDAwMDAzMWZmMGYwNTAwMjYxZjE4NGEzYjAzNDIwMDQ3MGEwMDQyMDMyZTA0MzI0MTQ0MzEwNDRjMDAyZTczNjg3Mzc0NzI3NDYxNjIwMDJlNzQ2NTc4NzQwMDJlNjQ2MTc0NjEwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMGIwMDAwMDAwMTAwMDAwMDA3MDAwMDAwMDAwMDAwMDA4MDAwNDAwMDAwMDAwMDAwODAwMDAwMDAwMDAwMDAwMDMzMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMTAwMDAwMDAxMDAwMDAwMDMwMDAwMDAwMDAwMDAwMGI0MDA0MDAwMDAwMDAwMDBiNDAwMDAwMDAwMDAwMDAwMTUwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwNDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMDAwMDAwMDMwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMGM5MDAwMDAwMDAwMDAwMDAxNzAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAw>)
- execute resulting binary

---

<details><summary>FLAG:</summary>

```
WPI{l4s1x;1s4_5crub5}
```

</details>
<br/>
