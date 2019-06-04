#### Challenge:

Agent, we have obtained a network traffic capture, which was recorded at enemy headquarter. At that time, one of the foreign agents (we suppose it was agent "Mc Pew") connect his device to the network. Analyze the traffic and try to find any useful information. Good luck Agent, [dhcp.pcap.gz](./dhcp.pcap.gz ':ignore')

---

#### Solution:

```bash
tshark -O SIP -nr ./dhcp.pcap -2 -R 'ip.dst_host matches "10.0.1.4"' -T fields -e bootp.hw.mac_addr
```

[CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')&input=NDM6NTQ6MzE6Mzg6MmQ6NDIKNjI6MzE6NjE6MmQ6NTk6NDUKNjU6NTI6MmQ6NzI6MzY6NTMKNjE6MmQ6NzI6NGE6NjE6NmY)

---

<details><summary>FLAG:</summary>

```
CT18-Bb1a-YEeR-r6Sa-rJao
```

</details>
