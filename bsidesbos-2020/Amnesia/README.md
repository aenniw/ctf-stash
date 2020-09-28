#### Challenge:

Ohh no! I can't remember anything, where have I been? <br><br> <b>Download the file below. Note, this is a large 1GB file and may take some time to download.</b> <br><br> <a class="btn btn-info btn-file mb-1 d-inline-block px-2 w-100 text-truncate" href="https://johnhammond.org/static/misc/image.bin"><i class="fas fa-download"> </i><small>image.bin</small></a>

---

#### Solution:

```bash
volatility -f image.bin imageinfo
volatility -f image.bin --profile=Win7SP1x86 pslist
git clone https://github.com/superponible/volatility-plugins.git
volatility --plugins=./volatility-plugins -f image.bin --profile=Win7SP1x86 chromehistory
```

---

<details><summary>FLAG:</summary>

```
flag{forensic_cookie_hunter}
```

</details>
<br/>
