#### Challenge:

Hi Commander,

with the patch "installed", we opened the way to an initiation ritual that would allow us to become a Berserker. The process is fully automated - we have discovered that you have to run some downloaded code, acquire unique password (co called `B-code`) and enter it to the web in given time limit. You have to overcome some difficulties, of course.

Visit [Berserker's web](http://challenges.thecatch.cz/781473d072a8de7d454cddd463414034), there you can download your initiation challenge. The acquired code should be returned to the web in GET request in parameter `answer`.

---

#### Solution:

```python
#!/usr/bin/env python3

import requests
from requests import session
from itertools import permutations
import base64
import hashlib
import re
import os
import subprocess


def allPermutations(str):
    permList = permutations(str)

    opts = []
    for perm in list(permList):
        opts.append(''.join(perm))

    return opts


def fix_word(data, w):
    for f in allPermutations(w):
        data = data = data.replace(f, w)
    return data


def base64ToString(b):
    return base64.b64decode(b + '===').decode('utf-8')


url = "http://challenges.thecatch.cz/781473d072a8de7d454cddd463414034"
tmp_file = "/tmp/file.py"


def fix_file(ses):
    resp = ses.get(url).text
    data, check = resp.split('\n')[0].split(': ')[1].split(';')

    data = base64ToString(data.strip())
    check = base64ToString(check.strip())

    data = fix_word(data, 'return')
    data = fix_word(data, 'import')
    data = fix_word(data, 'def')
    data = fix_word(data, 'main')
    data = data.replace('+ =', '+=')
    data = data.replace('res +=', '\tres +=')
    data = data.replace(':\n"""', ':\n\t"""')
    data = data.replace('\t\telse:\n\t\tvalue', '\t\telse:\n\t\t\tvalue')
    data = re.sub(r'\telse\n', '\telse:\n', data)

    data = re.sub(r'enumerate\(code\):\n.*if',
                  'enumerate(code):\n\t\tif', data)
    data = re.sub(r'2 == 0:\n.*res', '2 == 0:\n\t\t\tres', data)
    data = re.sub(r'2 == 0:\n.*value', '2 == 0:\n\t\t\tvalue', data)
    data = re.sub(r'> 0:\n.*if', '> 0:\n\t\tif', data)
    data = re.sub(r'\n.*code = res\n', '\n\t\tcode = res\n', data)

    data_fixed = ''
    for l in data.split('\n'):
        if 'if' in l.strip() and l.strip()[-1:] != ':':
            data_fixed += l+":\n"
        else:
            data_fixed += l+"\n"
    data = data_fixed

    with open(tmp_file, "w") as text_file:
        text_file.write(data)

    return check


flag = ''
while 'FLAG' not in flag:
    try:
        ses = session()
        check = fix_file(ses)
        os.system('chmod +x '+tmp_file)
        result = subprocess.check_output(tmp_file+' -n ' + check, shell=True)
        result = str(result).split(': ')[1].split('\\')[0].strip()

        flag = ses.get(url + '?answer='+str(result)).text
    except:
        pass

print(flag)
```

---

<details><summary>FLAG:</summary>

```
FLAG{A92w-i3vS-jBJB-B8A6}
```

</details>
