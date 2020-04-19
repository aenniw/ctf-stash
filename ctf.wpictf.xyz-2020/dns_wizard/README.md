#### Challenge:

Can you find it?

---

#### Solution:

```bash
dig wpictf.xyz TXT +short | tr -d '"' | base64 -d
```

---

<details><summary>FLAG:</summary>

```
WPI{1F0und_Th3_DNS-record}
```

</details>
<br/>
