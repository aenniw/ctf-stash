#### Challenge:

Find me!
Challenge created by Security Risk Advisors for RITSEC CTF [findme.pcap](./findme.pcap ":ignore")

---

#### Solution:

```bash
nc  18.219.169.113 1337 | base64 -d > payload.unknown
binwalk -e payload.unknown
grep -r "RITSEC" ./_payload.unknown.extracted/
```

---

<details><summary>FLAG:</summary>

```
RITSEC{pcaps_0r_it_didnt_h@ppen}
```

</details>
<br/>
