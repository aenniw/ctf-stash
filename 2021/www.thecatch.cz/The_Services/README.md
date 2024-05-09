#### Challenge:

Hi Expert,

examine the services on new discovered server `78.128.216.6` in order to have a comprehensive picture.

Good Luck!

---

#### Solution:

Running this `nmap` for service discovery:

```
sudo nmap -sS -sV -sC -vv 78.128.216.6
```

Reveals three out of four parts of the flag in the `fingerprints` of various services open on the server (HTTP, SSH, Samba). The last discovered service was FTP. Simply connecting to it reveals the last part of the flag. Composing the parts and decoding the result as `base64` gets us the final flag.

---

<details><summary>FLAG:</summary>

```
FLAG{Yrc7-W3qV-FMk2-49yW}
```

</details>
<br/>
