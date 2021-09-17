#### Challenge:

Climb on the Magic Modbus and see if you can find some of the messages being passed around! [modbus.pcap](./modbus.pcap ":ignore")

---

#### Solution:

- decoding the `modbus` `regval` field per source address reveals communication between devices with flag
```console
OK Bus, do your stuff!
If you keep asking questions, you'll keep getting answers!
flag{Ms_Fr1ZZL3_W0ULD_b3_s0_Pr0UD}
```

```bash
for ord in $(tshark -r ./modbus.pcap -T fields -e modbus.regval_uint16 -Y 'ip.src == 238.0.0.6'); do
    printf "\\$(printf '%03o' "$ord")";
done;
echo
```

---

<details><summary>FLAG:</summary>

```
flag{Ms_Fr1ZZL3_W0ULD_b3_s0_Pr0UD}
```

</details>
<br/>
