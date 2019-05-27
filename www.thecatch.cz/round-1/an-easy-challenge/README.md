#### Challenge:

This morning we got an anonymous tip - somebody dropped a USB drive into our mailbox without any additional information. The drive contained a single file. Your fellow agents have analyzed the rest of the drive and haven't found anything suspicious. Is this a red herring or could this mysterious file lead us somewhere? Our Crypto team suggested we put You on the case. Agent, do your best! [Groups.xml](./Groups.xml)

---

#### Solution:

```json
[
  { "op": "From Base64",
    "args": ["A-Za-z0-9+/=", true] },
  { "op": "To Hex",
    "args": ["None"] },
  { "op": "AES Decrypt",
    "args": [{ "option": "Hex", "string": "4e 99 06 e8  fc b6 6c c9  fa f4 93 10  62 0f fe e8 f4 96 e8 06  cc 05 79 90  20 9b 09 a4  33 b6 6c 1b" }, { "option": "Hex", "string": "" }, "CBC", "Hex", "Hex", { "option": "Hex", "string": "" }] },
  { "op": "From Hex",
    "args": ["Auto"] }
]
```

[CyberChef](https://gchq.github.io/CyberChef/)

---

<details><summary>FLAG:</summary>

```
CT18-jSDi-KuMI-JNue-um3q
```

</details>
