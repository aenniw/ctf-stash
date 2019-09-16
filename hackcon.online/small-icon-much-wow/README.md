#### Challenge:

One of my friends like to hide data in images.Help me to find out the secret in image. [stego.jpg](./stego.jpg ":ignore")

---

#### Solution:

```bash
binwalk ./stego.jpg
dd if=./stego.jpg of=./img.jpg bs=1 skip=202
zbarimg ./img.jpg
```
---

<details><summary>FLAG:</summary>

```
d4rk{flAg_h1dd3n_1n_th3_thumbnail}c0de
```

</details>
