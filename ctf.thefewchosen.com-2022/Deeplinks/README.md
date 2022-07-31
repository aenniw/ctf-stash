#### Challenge:

My intern configured my iOS app and my website to handle deeplinks, but they didn't tell me the path :( Can you help me find it?

---

#### Solution:

Googling a bit about `deeplinks` and `ios` lead me to this [site](https://developer.apple.com/library/archive/documentation/General/Conceptual/AppSearch/UniversalLinks.html). There I found out that there is a file similar to `robots.txt`, but for `ios` deeplinks to the website - `.well-known/apple-app-site-association`.

From there it is simple:

```
curl http://01.linux.challenges.ctf.thefewchosen.com:52031/.well-known/apple-app-site-association
```

---

<details><summary>FLAG:</summary>

```
TFCCTF{4ppl3_4pp_51t3_4550c14t10n}
```

</details>
<br/>
