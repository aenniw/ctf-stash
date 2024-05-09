#### Challenge:

Sometimes things that are broken have been broken on purpose. [broken.img](../broken.img ":ignore")

---

#### Solution:

```bash
file ./_broken.zip.extracted/broken/broken.img
mkdir broken
sudo mount -o loop ./_broken.zip.extracted/broken/broken.img ./broken
fsck.ext4 ./_broken.zip.extracted/broken/broken.img
sudo mount -o loop ./_broken.zip.extracted/broken/broken.img ./broken
sudo chmod 777 -R ./broken
grep -R 'TUCTF' ./broken/
```

---

<details><summary>FLAG:</summary>

```
TUCTF{D1S4ST3R_R3C0V3RY}
```

</details>
<br/>
