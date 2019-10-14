## Walk the bin out

I can make this easy just by telling you the tool or maybe you can read the title again and figure out your self. [walk.jpg](./walk.jpg ":ignore")
P.S - It's a very famous, open source tool :)

```bash
binwalk -Me walk.jpg
cat _walk.jpg.extracted/29A72 | tail -2 | base64 -d | base32 -d
```
<details><summary>FLAG:</summary>

```
tryhackme{b1nw4lk_0r_f0r3mo5t}
```

</details>
