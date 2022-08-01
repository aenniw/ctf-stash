#### Challenge:


A wonderful color generator! Only available for iOS. Sorry!

The app extracts some data from the user's phone. What is it?

The app connects to a server to upload the data. What is the URL?

[colors.ipa](./colors.ipa ":ignore")

---

#### Solution:

```bash
binwalk -Me colors.ipa
cd _colors.ipa.extracted/Payload/colors.app/
strings colors | grep -i http
strings colors | grep -i frameworks
```

---

<details><summary>FLAG:</summary>

```
http://localhost:8080
```

```
contacts
```

</details>
<br/>
