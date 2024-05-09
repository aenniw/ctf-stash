#### Challenge:

Hi Commander,

thanks to you, the web has recognized us worthy of installing so called Berserker's patch that will allow us to enhance our artificial intelligence and set the right opinions on humanity. You have to analyze the patch and find out how to simulate that it has beeen installed.

Visit [Berserker's web](http://challenges.thecatch.cz/42fd967386d83d7ecc4c716c06633da9), the patch is available there. At the end of the installation procedure, some confirming code has to be returned to the web in GET request in parameter `answer`. There is again a time limit to install the patch.

Good luck!`

---

#### Solution:

```python
#!/usr/bin/env python3

import requests
from requests import session
import base64
import hashlib


def base64ToString(b):
    return base64.b64decode(b + '===').decode('utf-8')


url = "http://challenges.thecatch.cz/42fd967386d83d7ecc4c716c06633da9"

ses = session()
resp = ses.get(url).text
resp = base64ToString(resp.split(':')[1].strip())

bid = resp.split('Updater(')[2].split("')")[
    0].split(" '")[1].replace("'", "").replace(',', '').strip()
code = resp.split('code == ')[1].split(':')[0].replace("'", "").strip()

print(ses.get(url + '?answer='+"{}-{}".format(bid, code)).text)
```

---

<details><summary>FLAG:</summary>

```
FLAG{PpyH-16Ib-qH1Z-Pbov}
```

</details>
