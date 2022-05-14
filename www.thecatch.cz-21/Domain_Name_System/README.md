#### Challenge:

Hi Expert,

the archaeologists have found valuable source of information - a DNS server running on `78.128.216.18`. Examine it and found as much information as possible.

Good Luck!

---

#### Solution:

First I did reverse lookup of the servers own ip `78.128.216.18` to get the domain it serves (`super.tcc.`). Then I tried `AXFR` - `DNS zone transfer` to dump it whole. One of the returned `TXT` records was base64 encoded flag.

```bash
dig @78.128.216.18 -x 78.128.216.18
dig @78.128.216.18 super.tcc. axfr
```

---

<details><summary>FLAG:</summary>

```
FLAG{zh71-iouQ-bxms-jwHk}
```

</details>
<br/>
