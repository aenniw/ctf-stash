#### Challenge:

Hi Expert,

some confused archaeologist brings you encrypted zip file and some text string which should leads to password. Then points on it, muttered something about crazy times, and left. Prove your skill and get the password for file.

Download the file [`encrypted_archive.zip`](./encrypted_archive.zip ":ignore")

---

#### Solution:

Unzipping the provided `ZIP` archive gives two files - `lead_to_password.txt` containing `8fd2011515522f6879dddd55d18a83d7` and encrypted `treasure_map.zip`.  Obviously the lead is hash, feeding it to [https://crackstation.net/](https://crackstation.net/) returns `mytreasure`. The rest is clear.

---

<details><summary>FLAG:</summary>

```
FLAG{q5hi-Pa72-dxbp-wRHf}
```

</details>
<br/>
