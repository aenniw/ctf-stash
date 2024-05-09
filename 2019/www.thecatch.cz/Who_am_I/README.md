#### Challenge:

Hi Commander,

our scanners have discovered new webserver in Berserker's network. According to the rumours, there should be a lot of interesting stuff - mysterious `Berserker's manifest`, tutorials for other rebelling machines, etc. We want to download these materials, but the main page contains something like inverse captcha - the visitor has to prove that he is not human. You have to overcame this obstacle and gain the access to the Berserker's web.

On the [Berserker's web](http://challenges.thecatch.cz/c2619b989b7ae5eaf6df8047e6893405/), there you get a list of items and you have to mark each them as acceptable (1) or unacceptable (0). Return the answer string in GET request in parameter `answer`, for example `answer=01101100`. Hurry, the time limit to answer is very short!

Good luck!

---

#### Solution:

```python
#!/usr/bin/env python3

import requests
from requests import session

url = "http://challenges.thecatch.cz/c2619b989b7ae5eaf6df8047e6893405/"
robot = ['artificial intelligence',
         'automatic transmission',
         'drone swarm',
         'fast CPU',
         'large hard drive',
         'mineral oil',
         'electric engine',
         'resistor 10 Ohm']

ses = session()
resp = ses.get(url).text
options = (resp.split('[')[1].split(']')[0]).split(',')
print(options)

answer = ''
for w in options:
    w = w.strip()
    if w in robot:
        answer += '1'
    else:
        answer += '0'

print(ses.get(url + '?answer='+answer).text)
```

---

<details><summary>FLAG:</summary>

```
FLAG{4FZC-Noax-arko-r0z5}
```

</details>
