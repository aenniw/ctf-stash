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

alternative solution:

```python
#!python3
# -*- coding: utf-8 -*-

import os
import email
from email import policy
from email.parser import BytesParser
import re
import requests

SOURCE_DIR = '.'

def find_urls_in_string(string):
    regex = r"(?i)\b((https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)
    return [x[0] for x in url]

def find_flag_in_string(string):
    regex = r"FLAG\{.{4}-.{4}-.{4}-.{4}\}"
    matches = re.findall(regex,string)
    return matches

def main():
    urls = []

    files = [f for f in os.listdir(SOURCE_DIR) if os.path.isfile(os.path.join(SOURCE_DIR, f))]

    for file in files:
        with open(file, 'rb') as file_handle:
            msg = BytesParser(policy=policy.default).parse(file_handle)

        text = msg.get_body(preferencelist=('plain')).get_content()
        urls = find_urls_in_string(text)

        for url in urls:
            try:
                response = requests.get(url)
                flag = find_flag_in_string(response.text)
                if flag:
                    print(flag)
            except:
                print("error for url: ", url)

    return True

if __name__ == "__main__":
    main()

```

---

<details><summary>FLAG:</summary>

```
FLAG{Tyqz-EgrI-8G7E-6PKB}
```

</details>
<br/>
