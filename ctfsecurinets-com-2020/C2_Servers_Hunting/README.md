#### Challenge:

The Emperor accidentally installed a malware that made him lose everything because his credentials got stolen.

After analyzing his computer, we found multiple network communications with these domains:

`c2-securinets-2020.info`

`c2-securinets-2020.ovh`

`c2-securinets-2020.com`

`c2-securinets-2020.site`

Could you try to find the owner of at least one of these domains ?

The flag is in the owner name. You will find the flag already in this format Securinets{}. If you didn't find this, so you didn't find the flag.

---

#### Solution:

When checking the domains with `whois` I noticed that `c2-securinets-2020.com` was updated after creation. After searching for ways to read whois history I have came upon site [whoxy.com](https://www.whoxy.com/), which revealed previous owner. It's noteworthy that this site is online whois tool keeping also whois domain history and able to do reverse whois lookup for `Owner's Name`, `E-mail Address`, `Company Name` and  `Domain Keyword`.

```bash
curl -sS "https://www.whoxy.com/c2-securinets-2020.{info,ovh,com,site}#history" | grep -i -o "Securinets{.*}"
```

---

<details><summary>FLAG:</summary>

```
Securinets{Emper0r_Of_C2_Serv3rs}
```

</details>
<br/>
