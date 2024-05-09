#### Challenge:

Oh no! I found some spyware on my laptop.  Can you find out what the attacker saw? [capture.pcap](./capture.pcap ":ignore")

---

#### Solution:

We are given network capture containing `HTTP` communication with many `JPEG` images. Extracting them using `foremost` and viewing them in order (like video) we are able to read the flag.

```bash
formost -v -i capture.pcap
```

---

<details><summary>FLAG:</summary>

```
flag{i_spy_with_my_little_eye}
```

</details>
<br/>
