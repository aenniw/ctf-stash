#### Challenge:

Hi, junior investigator! 

We have extracted a bunch of suspicious e-mails. We believe that you can analyze them and find their secret. [malicious_emails.tar.xz](./malicious_emails.tar.xz ":ignore")

Good Luck!

---

#### Solution:

```bash
#!/bin/bash

for f in ./*.eml; do
    msg=$(awk '/Content-Transfer-Encoding: base64/{flag=1; next} /--===============/{flag=0} flag' ${f})
    
    urls=$(echo ${msg} | grep -q -v 'Content-Disposition:' && \
            echo ${msg} | base64 -i -d | egrep -o 'https?://[^ ]+')
    for url in ${urls}; do
        curl ${url} 2>/dev/null | grep FLAG
    done
done
```

---

<details><summary>FLAG:</summary>

```
FLAG{Tyqz-EgrI-8G7E-6PKB}
```

</details>
<br/>
