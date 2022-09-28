#### Challenge:

What a nice spot to have a picnic, EXAMINE the image and discover where this was taken.

Flag format: The name of the area with no spaces, case insensitive

[view.jpg](./view.jpg ":ignore")

---

#### Solution:

Word `EXAMINE` and the name of the challenge hint to `exif` and `GPS`.

Running:

```bash
exiftool view.jpg | grep "GPS Position"
```

Gives:

```text
GPS Position: 27 deg 28' 6.69" S, 152 deg 58' 10.10" E
```

Googling the coordinates yields the flag.

---

<details><summary>FLAG:</summary>

```
HoopPine
```

</details>
<br/>
