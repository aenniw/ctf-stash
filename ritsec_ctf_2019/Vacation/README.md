#### Challenge:

These are my favorite places to visit [http://us-central-1.ritsec.club/l/chromebin](https://drive.google.com/uc?export=view&id=1ff3A5fmY0PBwTm6HBKC-5MqbBsCXJv1t)

---

#### Solution:

```bash
unlzma chromebin.lzma
mv chromebin chromebin.tar
tar -xf chromebin.tar 'Chrome/User Data/Default/Bookmarks'
cat  'Chrome/User Data/Default/Bookmarks' | jq .roots.other.children[].name | tr -d '"' | tr -d "\n"
```

---

<details><summary>FLAG:</summary>

```
RITSEC{CHR0M3_BM_FTW}
```

</details>
<br/>
