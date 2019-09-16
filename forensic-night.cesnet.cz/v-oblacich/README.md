#### Challenge:

Pozorování oblaků letících po obloze je ukliďnující, ale jen do doby než zjistíte, že se v nich skrývá hledaný flag. [clouds.mp4.gz](./clouds.mp4.gz ":ignore")

---

#### Solution:

```bash
ffmpeg -i ../clouds.mp4 -vf fps=60 frame-%d.png # manually inspect each frame
```

---

<details><summary>FLAG:</summary>

```
flag{Jimmy_Donal-1640}
```

</details>
