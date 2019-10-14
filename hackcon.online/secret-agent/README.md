#### Challenge:

Not so [secret](http://68.183.158.95/secret_agent/) after all?

---

#### Solution:

```bash
curl -v http://68.183.158.95/secret_agent/ -H "User-Agent: $(curl http://68.183.158.95/secret_agent/)"
```

---

<details><summary>FLAG:</summary>

```
d4rk{useragent_ftwwwwwww}c0de
```

</details>
