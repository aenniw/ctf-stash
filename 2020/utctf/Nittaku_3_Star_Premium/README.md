#### Challenge:

I found some weird data while monitoring my network, but I didn't catch it all. See if you can make sense of it. [capture.pcap](./capture.pcap ":ignore")

---

#### Solution:

- after inspection of `pcap` ICMP trafic contains part of `gz` content
- after capturing the ICMP trafic and executing `ping pingable.tk` the whole file can be retrieved

```bash
tshark -r ./icmp.pcapng  -T fields -e data  -Y 'icmp and data.len gt 100' | tr -d '\n' |  xxd -r -p | base64 -d  > flag.png.gz
```

---

<details><summary>FLAG:</summary>

```
utflag{p1Ng@b13_f1aG$}
```

</details>
<br/>
