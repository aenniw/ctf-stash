#### Challenge:

Kira loves to watch Scooby Doo so much that she made a website about it! She also added a clicker game which looks impossible. Can you use your inspector skills from Pink Panther to reveal the flag?

http://scoobydoo.web.2019.nactf.com

---

#### Solution:

```bash
wget -f http://scoobydoo.web.2019.nactf.com/game.html
sed -i 's/opacity:.*; //' ./scoobydoo.web.2019.nactf.com/game.html
firefox ./scoobydoo.web.2019.nactf.com/game.html
```

---

<details><summary>FLAG:</summary>

```
nactf{ult1m4T3_sh4ggY}
```

</details>
