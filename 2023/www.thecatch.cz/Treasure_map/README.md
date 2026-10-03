#### Challenge:

Ahoy, deck cadet, 

working with maps and searching for treasures is every sailor's daily routine, right? Your task is to examine the map and find any hidden secrets.

May you have fair winds and following seas!

Download the [treasure_map.zip](./treasure_map.zip ":ignore"). \
(MD5 checksum: `4f0f6570025ded4d7823739bc963d85e`)

---

#### Solution:

The archive holds a single file, `treasure_map.png` – a parchment-style pirate map
whose landmarks are all networking terms (`Ethernet Mountains`, `IPv6 Hills`,
`ARP Sea`, …) and with a red **X** marking a spot labelled **`Wi-Fi AP`**. The task
is to find the map's "hidden secret".

First I ruled out the usual carrier tricks: the PNG is clean – nothing is appended
after the `IEND` chunk, the only ancillary chunks are an empty `tEXt`/`pHYs`, the
whole IDAT stream decompresses with no trailing bytes, and the LSB planes just track
the visible drawing (no embedded file). So the secret is drawn *into the picture*
itself.

Sampling pixels shows the map uses a very limited palette: the parchment background
is `#c79d6c` and the land is `#a97e52`. Scattered over the background, however, there
are tiny strokes in a slightly **lighter** shade, `#d9b484`, that are almost
invisible to the eye. Selecting just that colour (GIMP → *Select by Colour*, or a
big saturation/contrast boost, or ImageMagick below) makes them pop out: about twenty
small, hand-drawn, randomly-rotated capital letters dotted all across the map.

```bash
unzip treasure_map.zip                 # -> treasure_map.png (4533x3173 RGB)

# background #c79d6c, land #a97e52, hidden letters are the lighter #d9b484.
# Reveal: paint the hidden shade red and everything else white.
magick treasure_map.png -fuzz 5% \
       -fill '#ff0000' -opaque '#d9b484' \
       -fill '#ffffff' +opaque '#ff0000' revealed.png
# (equivalent manual method: open in GIMP and crank Colours -> Saturation + Contrast,
#  or Select by Colour on a lighter tan pixel.)
```

Collecting the revealed glyphs and undoing their rotations yields ~20 letters.
Among them the word `FLAG` is spelled out, and the rest unscramble into the short,
sailor-themed phrase the pirate map was hiding – which, written in the challenge's
`FLAG{....-....-....-....}` format, is the flag.

---

<details><summary>FLAG:</summary>

```
FLAG{WIFI-AHEA-DCAP-TAIN}
```

</details>
<br/>
