#### Challenge:

Ahoy, officer,

after a reboot at 2023-10-02 11:30:18 UTC, the On-board signal flag recognition system (OBSF-RS) has malfunctioned. The signal flags are no more recognized and the only working function is to generate and save schematic views, which are created every time a ship in the vicinity changes its signaling. We need to know what the surrounding ships signaled and if we have missed something important.

May you have fair winds and following seas!

Download the [signal_flags.zip](./signal_flags.zip ":ignore").\
(MD5 checksum: `c1820a3c41a0d6a0daacd84b69fd1b57`)

---

#### Solution:

The archive holds 90 PNG schematics named `signalization_*.png`. Each one draws a
single ship at one instant, with a row of **international maritime (ICS) signal
flags** hoisted along the fore-stay, every flag boxed by a green recognition
frame. On the side the OBSF-RS prints metadata: a GMT timestamp, a 6-digit *ship
object ID*, the number of flags and the *signal type*. The flags themselves are
left untranslated (`Signal content: <Unknown>`), so my whole job is to recognise
them myself and read what the ships were saying — "just grab a shovel and dig".

**Reading the flags.** The flags are standard ICS flags (e.g. white with a red
saltire = *Victor*, an all-red swallowtail = *Bravo*, a red diamond on white =
*Foxtrot*). I never look them up by hand 90 times; I script it with OpenCV:

* Every flag lives inside a *closed* green rectangle. If I take the "not green"
  mask, each box interior becomes its own connected component that does not touch
  the image border — so the boxes separate cleanly even on a crowded halyard
  where the frames overlap. The one oversized box per picture is the national
  **ensign** (the ship's nationality) and I drop it.
* I crop the coloured content of each box, downscale it, and greedily cluster the
  1200+ crops. That collapses to ~30 distinct flag designs. Dumping one sample
  per cluster and eyeballing it against an ICS chart gives me a design→meaning
  table.

**The encoding.** The short hoists spell plain words directly in ICS letters
(e.g. `VERICH`, `IMPROVE`). The long hoists all start with the *same* two-flag
preamble and are built almost entirely from the **numeral pennants** plus the
alphabet flags **A–F**. That is the giveaway: it is **hex**. The alphabet flags
`A`…`F` are the hex nibbles `0xA`…`0xF`, the numeral pennants `0`…`9` are the
nibbles `0x0`…`0x9`, and each *pair* of flags is one byte. Pairing up and
decoding as ASCII turns the long hoists into readable English chatter.

**Finding the important bit.** Grouping the decoded hoists by ship object ID and
ordering them by timestamp reassembles each ship's full transmission. Most of it
is harmless small-talk — a broken coffee machine, a party on the bridge at 2100
ZULU, free pinot gris, and everyone relaying *"Have you seen Mr. Caletka?"*. One
ship (`CNS Josef Verich`, object ID `717609`) slips in something that is *not*
English: a Base64 blob spread across several consecutive hoists —
`...you can ... them by RkxBR3tsVHJHLTNvWG4tYW9aTi1aNHFNfQ== !`. Base64-decoding
it gives the flag. That is the "something important" I'd have missed by only
skimming the chatter.

I put the whole pipeline into one script (`decode_signal_flags.py`):

```python
#!/usr/bin/env python3
"""Recognise the ICS signal flags in every OBSF-RS schematic and read the message.
    python3 decode_signal_flags.py <dir with signalization_*.png>
Needs: opencv-python, numpy, and tesseract for the on-image metadata."""
import sys, os, glob, re, base64, subprocess
import cv2, numpy as np

SRC = sys.argv[1] if len(sys.argv) > 1 else '.'

def flags_of(img):
    # Each flag sits in its own closed green box; a box interior is a connected
    # component of the 'not green' mask that does not touch the image border, so
    # overlapping frames still separate. The oversized box is the ensign -> skip.
    # Flags are read from the masthead downwards (top = smallest y).
    H, W = img.shape[:2]
    b, g, r = cv2.split(img.astype(int))
    green = (g > 150) & (r < 100) & (b < 100)
    notg = 1 - cv2.dilate(green.astype(np.uint8), np.ones((3, 3), np.uint8))
    n, _, st, _ = cv2.connectedComponentsWithStats(notg, 4)
    cells = [(x, y, w, h) for x, y, w, h, a in st[1:]
             if 1 < x and 1 < y and x + w < W - 1 and y + h < H - 1
             and 20 < w < 120 and 20 < h < 160 and a > 300]
    cells.sort(key=lambda c: c[1])
    sigs = []
    for x, y, w, h in cells:
        sub = img[y:y+h, x:x+w]
        bb, gg, rr = cv2.split(sub.astype(int))
        bg  = (abs(bb-221) < 28) & (abs(gg-222) < 28) & (abs(rr-222) < 28)
        grn = (gg > 150) & (rr < 100) & (bb < 100)
        m = cv2.morphologyEx(((~bg) & (~grn)).astype(np.uint8), cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
        nn, _, stt, _ = cv2.connectedComponentsWithStats(m, 8)
        if nn <= 1:
            sigs.append(None); continue
        ci = 1 + int(np.argmax(stt[1:, 4]))
        cx, cy, cw, ch, _ = stt[ci]
        sigs.append(cv2.resize(sub[cy:cy+ch, cx:cx+cw], (24, 16),
                               interpolation=cv2.INTER_AREA).astype(np.float32).flatten())
    return sigs

def meta(path):                     # read the printed timestamp + ship object ID
    txt = subprocess.run(['tesseract', path, '-', '--psm', '6'],
                         capture_output=True, text=True).stdout
    ts  = re.search(r'GMT\s*([\d:\- ]+)', txt)
    oid = re.search(r'object ID[:\s]*(\d+)', txt)
    return (ts.group(1).strip() if ts else '?'), (oid.group(1) if oid else '?')

# 1. segment every flag of every schematic
files = sorted(glob.glob(os.path.join(SRC, 'signalization_*.png')))
per_file, inst = {}, []
for f in files:
    seq = []
    for s in flags_of(cv2.imread(f)):
        seq.append(None if s is None else len(inst))
        if s is not None: inst.append(s)
    per_file[f] = seq

# 2. cluster the identical flag renderings (deterministic greedy)
cent, labels = [], []
for s in np.array(inst):
    d = [np.mean((c - s) ** 2) for c in cent]
    j = int(np.argmin(d)) if d else -1
    if j >= 0 and d[j] < 230:
        k = labels.count(j); cent[j] = (cent[j] * k + s) / (k + 1); labels.append(j)
    else:
        cent.append(s.copy()); labels.append(len(cent) - 1)

# 3. design -> value table, read once off a per-cluster montage:
#    alphabet flags A..F = hex nibbles 0xA..0xF, numeral pennants 0..9 = 0x0..0x9,
#    two flags = one ASCII byte, and every hex hoist starts with a 2-flag preamble.
HEX = {0:0x0, 5:0x1, 11:0x2, 3:0x3, 2:0x4, 7:0x5, 4:0x6, 8:0x7, 14:0x8, 12:0x9,
       18:0xA, 9:0xB, 6:0xC, 17:0xD, 13:0xE, 10:0xF}
ENSIGN = 16                         # a small ensign that slips past the size filter

def decode(seq):
    s = [c for c in (labels[i] for i in seq if i is not None) if c != ENSIGN]
    if s[:2] == [0, 1]:
        s = s[2:]
    if len(s) % 2 or any(c not in HEX for c in s):
        return None                 # plain-letter hoist, not hex
    try:
        return bytes((HEX[s[i]] << 4) | HEX[s[i+1]] for i in range(0, len(s), 2)).decode('ascii')
    except Exception:
        return None

# 4. per ship, in time order, read the transmission and pull out the Base64 blob
ships = {}
for f, seq in per_file.items():
    ts, oid = meta(f)
    ships.setdefault(oid, []).append((ts, decode(seq)))

for oid, msgs in ships.items():
    text = ''.join(m for _, m in sorted(msgs) if m)
    print(f'ship {oid}: {text!r}')
    hit = re.search(r'[A-Za-z0-9+/]{30,}={0,2}', text)
    if hit:
        print('  -->', base64.b64decode(hit.group()).decode())
```

Running it over the extracted PNGs reads every ship's transmission and recovers
the flag:

```bash
$ unzip -q signal_flags.zip -d flags && python3 decode_signal_flags.py flags
ship 304622: 'CNS Josef Verich, nice flagCNS Josef Verich, is Mr. Caletka on board?Have you seen Mr. Caletka?'
ship 367676: 'Party on the bridge at 2100 ZULU.Free pinot gris for everyone!'
ship 487078: 'Our coffee machine is broken, we need a mechanic.'
ship 717609: 'CNS Josef , are your nets ok, too? ;-)CNS Josef , you can  them by RkxBR3tsVHJHLTNvWG4tYW9aTi1aNHFNfQ== !'
  --> FLAG{....-....-....-....}
ship 567874: 'Hey, what is your wifi P?Relay: Have you seen Mr. Caletka?'
ship 745387: 'Can you sell us some ipv4 addresses?Relay: Have you seen Mr. Caletka?'
ship 627912: 'Relay: Have you seen Mr. Caletka?'
ship 782535: 'CNS Josef Verich, can your network guy set up a router for us?'
```

The Base64 that `CNS Josef Verich` was quietly broadcasting decodes straight to
the flag.

---

<details><summary>FLAG:</summary>

```
FLAG{lTrG-3oXn-aoZN-Z4qM}
```

</details>
<br/>
