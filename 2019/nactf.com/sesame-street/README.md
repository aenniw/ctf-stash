#### Challenge:

Surprisingly, The20thDuck loves cookies! He also has no idea how to use php. He accidentally messed up a cookie so it's only available on the countdown page... Also why use cookies in the first place?

sesamestreet.web.2019.nactf.com

---

#### Solution:

```bash
curl "http://sesamestreet.web.2019.nactf.com/flag.php" -H "Cookie: session-time=1569260289" 2>/dev/null | grep nactf
```

---

<details><summary>FLAG:</summary>

```
nactf{c000000000ki3s}
```

</details>
