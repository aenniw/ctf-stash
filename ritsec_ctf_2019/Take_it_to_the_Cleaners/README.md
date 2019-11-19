#### Challenge:

Description: People hide things in images all the time! See if you can find what the artist forgot to take out in this one! [ritsec_logo2.png](./ritsec_logo2.png ":ignore")

---

#### Solution:

```bash
exiftool ./ritsec_logo2.png | grep -i comment
```

- [CyberChef](https://gchq.github.io/CyberChef/#input=UlZaSFJsSlFlMU5DUlZKQlJsWlFSbDlUVGxaWlJsOUtRa0ZIWDFWU1dVTmZURUpJWDFWU1JWSjk)

```json
[
  { "op": "From Base64", "args": ["A-Za-z0-9+/=", true] },
  { "op": "ROT13", "args": [true, true, 13] }
]
```

---

<details><summary>FLAG:</summary>

```
RITSEC{FORENSICS_FAILS_WONT_HELP_YOU_HERE}
```

</details>
<br/>
