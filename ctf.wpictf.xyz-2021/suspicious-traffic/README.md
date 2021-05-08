#### Challenge:

I got a hold of a packet capture between a suspicious client and server. It looks really strange, could you take a look?

[capture.pcapng](./capture.pcapng ":ignore")

---

#### Solution:

We are given a `PCAP` file. After inspecting it in the `wireshark`, I noticed weird `HTTP` messages with the "Continuation" info, containing always only one byte of data.

```csv
"71","1.997220","127.0.0.1","127.0.0.1","HTTP","46","Continuation"
```

Extracting the byte from all these messages reveals the flag:

```bash
tshark -r capture.pcapng -T fields -e data | grep 0a | sed s/0a//g | xxd -r -p
```

---

<details><summary>FLAG:</summary>

```
WPI{su3p1ci0uS_htTp}
```

</details>
<br/>
