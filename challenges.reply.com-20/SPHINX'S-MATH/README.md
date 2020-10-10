#### Challenge:

Virgilia reveals Zer0 began his travels in ancient Egypt. Zer0 plans to alter the history once he’s learned the secrets of the greatest Pharaohs, kings and commanders who ruled the world in his own timeline. Nevertheless, R-Boy needs to learn some Hieroglyphics, in case he needs it to communicate with the Egyptians. Help R-Boy understand and learn this ancient language!

http://codingbox4sm.reply.it:1338/sphinxsEquaji

---

#### Solution:

```python
#!/usr/bin/env python3

import requests
from requests import session
from sympy.parsing.sympy_parser import parse_expr
from sympy import Eq, Symbol as sym, solve

url = "http://codingbox4sm.reply.it:1338/sphinxsEquaji/"


def solve_eqs(resp):
    eqs = []
    constants = {}
    for line in resp.split('<div class="enigma">')[1].split('</div>')[0].splitlines():
        line = line.strip()
        if line != '':
            eq = line[3:-4]
            eq = eq.replace('<b style="color: red">?</b>', 'X')
            eq_new = ""
            for c in eq:
                if ord(c) > 256:
                    if c not in constants:
                        constants[c] = chr(ord('a') + len(constants))
                    eq_new += '*'+constants[c] + ' '
                else:
                    eq_new += c
            eqs.append(eq_new)

    sym_eqs = []
    for eq in eqs:
        lhs = parse_expr(eq.split('=')[0])
        rhs = parse_expr(eq.split('=')[1])
        sym_eqs.append(Eq(lhs, rhs))

    solved = solve(sym_eqs)
    for s in solved:
        if str(s) == 'X':
            return int(solved[s])

    exit(1)


def get_step(resp):
    return int(resp.split('<h2>')[1].split('</h2>')[0].strip().split(' ')[1])


ses = session()
resp = ses.get(url).text

step = get_step(resp)
while step < 513:
    answer = solve_eqs(resp)
    print("%d -> %d" % (step, answer))
    resp = ses.post(url + 'answer', data={'answer': answer}).text
    step = get_step(resp)

print(resp)
```

---

<details><summary>FLAG:</summary>

```
{FLG:F0r63t_7h3_4r4b1c-num3r4l5_hi3r06lyph5_w1ll_n3v3r-d13!}
```

</details>
