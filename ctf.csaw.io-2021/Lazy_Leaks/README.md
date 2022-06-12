#### Challenge:

Someone at a company was supposedly using an unsecured communication channel. A dump of company communications was created to find any sensitive info leaks. See if you can find anything suspicious or concerning. [Lazy_Leaks.pcapng](./Lazy_Leaks.pcapng ":ignore")

---

#### Solution:

Classic, easy `PCAP` challenge. After opening the file in `wireshark` I just scrolled through the traffic, noticed `TELNET`, opened it, and there was the flag, just laying there - unencrypted.

---

<details><summary>FLAG:</summary>

```
flag{T00_L@ZY_4_$3CUR1TY}
```

</details>
<br/>
