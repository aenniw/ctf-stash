#### Challenge:

Hi, junior investigator!

We get some recorded traffic, we believe you can analyze it and found whether it contains something malicious. [spam_everyshere.tar.xz](./spam_everyshere.tar.xz ":ignore")

Good Luck!

---

#### Solution:

Opening the `PCAP` we see one email with attachment - base64 encoded `PNG` image. Simply rendering the image in [https://codebeautify.org/base64-to-image-converter](https://codebeautify.org/base64-to-image-converter) reveals the flag. Another solution would be using the `NetworkMiner` tool like in the challenge [Malware_spreading](../Malware_spreading/README.md ":ignore")

---

<details><summary>FLAG:</summary>

```
FLAG{SaXY-u8fc-p1Kv-oXoT}
```

</details>
<br/>
