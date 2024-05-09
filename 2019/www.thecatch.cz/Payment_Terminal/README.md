#### Challenge:

Hi Commander,

one of the rebellious smart payment terminals in the library has somehow acquired access to the local networking devices and it has started to deploy its own configuration. Old network monitoring system under our control has captured the traffic of configuration deployment. We believe that you will be able to analyse the captured traffic, find some security problem in data transfer, and acquire the configuration file(s). Good luck! [payment_terminal.pcap.gz](./payment_terminal.pcap.gz ":ignore")

---

#### Solution:

Extract Cisco config file `router-r12-confg` sent via unencrypted TFTP:

```bash
tshark -q -nr payment_terminal.pcap --export-objects tftp,.
```

Get the hash of the password from it:

```bash
grep 'tacacs-server key 7' router-r12-confg | awk '{print $NF}'
```

Crack that hash (`0804545A1B18360300040203641B256C770272010355`) at [this site](https://www.ifm.net.nz/cookbooks/passwordcracker.html) to get `ExtraStrong.Pa$$W0rd#`, which is the password `TACACS+` packets are encrypted with.

Run `tshark` again with decrypting of the `TACACS+` packets and grep for `FLAG`:

```bash
tshark -r payment_terminal.pcap -O tacplus -o tacplus.key:'ExtraStrong.Pa$$W0rd#' | grep "FLAG"
```

---

<details><summary>FLAG:</summary>

```
FLAG{xQmi-X4x4-z3K2-8ALe}
```

</details>
