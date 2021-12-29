#### Challenge:

Hi Expert,

the web site accessible via `http://challenges.thecatch.cz/geography` has some kind of access protection based on used IP address. Try to overcome this obstacle and find out what is behind it.

Good Luck!

---

#### Solution:


```bash
curl -cookie cookie.txt --cookie-jar cookie.txt http://challenges.thecatch.cz/geography
# Fetch the appropriate proxy server based on response from  https://www.proxynova.com/proxy-server-list/country-rs/
curl -cookie cookie.txt --cookie-jar cookie.txt -x 93.86.63.73:8080 -L http://challenges.thecatch.cz/geography
```

---

<details><summary>FLAG:</summary>

```
FLAG{OlFY-P2U0-86he-qU4q}
```

</details>
<br/>
