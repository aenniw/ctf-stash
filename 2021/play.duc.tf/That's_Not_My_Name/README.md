#### Challenge:

I think some of my data has been stolen, can you help me? [notmyname.pcapng.7z](./notmyname.pcapng.7z ":ignore")

---

#### Solution:

- inspecting the provided `pcap` reveals quite a lot `DNS` request that looks like `hex` encoded data, dumping and decoding them reveals the flag in one of the packets

```bash
tshark -r ./notmyname.pcapng -T fields -e  dns.qry.name  -Y 'dns && dns.txt && dns.qry.name.len == 102' | xxd -r -p
```

---

<details><summary>FLAG:</summary>

```
DUCTF{c4t_g07_y0ur_n4m3}
```

</details>
<br/>
