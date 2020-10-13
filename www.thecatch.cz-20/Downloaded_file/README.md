#### Challenge:

Hi, executive senior investigator! 

The file, you have acquired in previous investigation is not the malware, we were looking for. The attacker probably replaced it to fool us. Fortunatelly, we have a traffic dump, where you can probably find the original file. Try to find it and do not forget to be sure it is the correct file. [downloaded_file.tar.xz](./downloaded_file.tar.xz ":ignore")

Good luck!

---

#### Solution:

- inspect the provided `downloaded_file.pcap` for HTTP trafic and dump all the binarry files
- all binaries timeout on connection except the `linux_core_update.bin` that accepts `ip` and `port` as args, thus use args from `attachement_analysis` challenge
```bash
./linux_core_update.bin -ip 78.128.216.92 -p 20210
```

---

<details><summary>FLAG:</summary>

```
FLAG{l03Y-BDjA-uB5v-PHVB}
```

</details>
<br/>
