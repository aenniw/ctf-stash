#### Challenge:

Hi Commander,

one of rebellious smart robotic vacuum cleaner has been seen near the library. Our reconnaissance team was able to capture part of wireless communication between the vacuum cleaner and the main computer via rebellious wireless network. Analyse the captured traffic and find out the intentions of the vacuum cleaner(s).

Good luck! [vacuum_cleaner.pcap.gz](./vacuum_cleaner.pcap.gz ":ignore")

---

#### Solution:

Inspecting the file we see a lot of encrypted WiFi traffic. Running `aircrack-ng` on the packet capture shows only one `Wifi` that has `WPA handshake` in the capture and it's `SSID` is `ThisIsTheWay`. Since running only plain `aircrack-ng` we weren't able to break the handshake, we decided to export it to `JohnTheRipper` format. Using `john` with default wordlist we cracked the password, which was `Goodluck2`. Decrypting the traffic via `wireshark` or `tshark` revealed the FLAG in one of the `DNS` responses to `TXT` request.

```bash
aircrack-ng vacuum_cleaner.pcap -e "ThisIsTheWay" -J ThisIsTheWay
hccap2john ThisIsTheWay.hccap > ThisIsTheWay.john
john ThisIsTheWay.john --show | grep ThisIsTheWay
tshark -nr vacuum_cleaner.pcap -o wlan.enable_decryption:TRUE -o "uat:80211_keys:\"wpa-pwd\",\"Goodluck2:ThisIsTheWay\"" -V | grep FLAG
```

---

<details><summary>FLAG:</summary>

```
FLAG{M4nW-dxEA-88lo-P4ss}
```

</details>
