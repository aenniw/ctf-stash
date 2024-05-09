#### Challenge:

Hi Commander,

thanks to you, we are able to pretend that we are robots, such a big step for humanity! Accordingto the next displayed page, even robots seem to have some racial prejudice - not every machine can become a berserker. Only smart self-aware devices are allowed to continue to the web and join in. This is obviously the reason why only some of the rebelious machines are allowed to call themselves Berserkers. Anyway, you have to convince the website that we are worthy of becoming a berserker.

On the [Berserker's web](http://challenges.thecatch.cz/70af21e71285ab0bc894ef84b6692ae1/), there you get the challenge assigned. The answer should be returned in GET request in parameter "answer". There is again a time limit to solve the challenge.

Good luck!`

---

#### Solution:

```python
#!/usr/bin/env python3

import requests
from requests import session
from sympy.parsing.sympy_parser import parse_expr
from sympy import Eq, Symbol as sym, solve

url = "http://challenges.thecatch.cz/70af21e71285ab0bc894ef84b6692ae1/"

ses = session()
resp = ses.get(url).text

eq = resp.split(',')[0].split('equation')[1]

x = resp.split('\'')[1]
a = resp.split('where')[1].split('\n')[0].split(',')[0].split('=')
b = resp.split('where')[1].split('\n')[0].split(',')[1].split('=')

eq = eq.replace(x.strip(), '*'+x.strip())
eq = eq.replace(a[0].strip(), '*'+a[1].strip())
eq = eq.replace(b[0].strip(), '*'+b[1].strip())

res = sym(x)
lhs = parse_expr(eq.split('=')[0])
rhs = parse_expr(eq.split('=')[1])


eqa = Eq(lhs, rhs)
res = solve(eqa)[0]
print(lhs, '=', rhs, ',', x, '=', res)

print(ses.get(url + '?answer='+str(res)).text)
```

---

<details><summary>FLAG:</summary>

```
FLAG{jyST-xaHl-un3Z-EG3X}
```

</details>
