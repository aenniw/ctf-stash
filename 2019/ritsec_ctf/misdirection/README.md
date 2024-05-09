#### Challenge:

Looks like someone gave you the wrong directions! http://ctfchallenges.ritsec.club:5000/ Flag format is `RS{ }`

---

#### Solution:

```bash
curl -L  -v 'http://ctfchallenges.ritsec.club:5000' 2>&1 | grep '> GET' | tr -d '/' | awk '{ print $3}' | tr -d '\n'
```

---

<details><summary>FLAG:</summary>

```
RS{4!way5_Ke3p-m0v1ng}
```

</details>
<br/>
