#### Challenge:

On the first leg of the journey, I was looking at all the life, there were plants and hills and rocks and things, there was java and mugs and caffeine. [broken.zip](./broken.zip ":ignore")

[chal.tuctf.com:32000](http://chal.tuctf.com:32000)

---

#### Solution:

```bash
curl http://chal.tuctf.com:32000/
curl -X BREW http://chal.tuctf.com:32000/teapot
curl -X BREW http://chal.tuctf.com:32000/broken.zip > broken.zip
binwalk -e ./broken.zip
cat ./_broken.zip.extracted/broken/flag.txt
```

---

<details><summary>FLAG:</summary>

```
TUCTF{d0_y0u_cr4v3_th3_418}
```

</details>
<br/>
