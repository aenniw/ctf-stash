#### Challenge:

I messed up prime generation, and now my private key doesn't work!

[generate.py](./generate.py ":ignore") [data.txt](./data.txt ":ignore")

---

#### Solution:

Obviously this is another one of my favorite crypto challenges - `RSA`. We know `N`, `e` and the `ciphertext`. We also know that `(p-1) is divisible by e^2` and `(q-1)` is also `divisible by e^2`.
This property is what breaks the decryption because the needed condition

`gcd(d, (p - 1) * (q - 1)) == 1`

doesn't hold. (More math details [here](https://crypto.stackexchange.com/questions/33676/why-do-we-need-eulers-totient-function-varphin-in-rsa)). I lost a lot of time by trying to recover the message using the algorithm provided in this [article](https://eprint.iacr.org/2020/1059.pdf) but it would only work if the `p-1` / `q-1` were divisible by `e` not `e^2`. Luckily thanks to that article I found this great [script/repository](https://github.com/jvdsn/crypto-attacks/blob/4f650cf18a459accc0789dd1f0dbf77003de5093/attacks/rsa/non_coprime_exponent.py), which has a fallback method for higher powers of `e` using `Adleman-Manders-Miller and CRT`. I'm not gonna pretend that I have any idea about how the math works there, but editing that file a bit by feeding the numbers to that module gave up the flag:

```python
import logging
import os
import sys
from math import gcd
from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes

from sage.all import GF
from sage.all import crt
from sage.all import is_prime

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(os.path.abspath(__file__)))))
if sys.path[1] != path:
    sys.path.insert(1, path)

from attacks.factorization import known_phi
from shared import rth_roots


def attack(N, e, phi, c):
    """
    Computes possible plaintexts when e is not coprime with Euler's totient.
    More information: Shumow D., "Incorrectly Generated RSA Keys: How To Recover Lost Plaintexts"
    :param N: the modulus
    :param e: the public exponent
    :param phi: Euler's totient for the modulus
    :param c: the ciphertext
    :return: a generator generating possible plaintexts for c
    """
    assert phi % e == 0, "Public exponent must divide Euler's totient"
    assert is_prime(e), "Public exponent must be prime"
    if gcd(phi // e, e) == 1:
        phi //= e
        # Finding multiplicative generator of subgroup with order e elements (Algorithm 1).
        g = 1
        gE = 1
        while gE == 1:
            g += 1
            gE = pow(g, phi, N)

        # Finding possible plaintexts (Algorithm 2).
        d = pow(e, -1, phi)
        a = pow(c, d, N)
        l = gE
        for i in range(e):
            x = a * l % N
            l = l * gE % N
            yield x
    else:
        # Fall back to more generic root finding using Adleman-Manders-Miller and CRT.
        p, q = known_phi.factorize(N, phi)
        tp = 0
        while (p - 1) % (e ** (tp + 1)) == 0:
            tp += 1
        tq = 0
        while (q - 1) % (e ** (tq + 1)) == 0:
            tq += 1

        assert tp > 0 or tq > 0
        cp = c % p
        cq = c % q
        logging.info(f"Computing {e}-th roots mod {p}...")
        mps = [pow(cp, pow(e, -1, p - 1), p)] if tp == 0 else list(rth_roots(cp, e, GF(p)))
        logging.info(f"Computing {e}-th roots mod {q}...")
        mqs = [pow(cq, pow(e, -1, q - 1), q)] if tq == 0 else list(rth_roots(cq, e, GF(q)))
        logging.info(f"Computing {len(mps) * len(mqs)} roots using CRT...")
        for mp in mps:
            for mq in mqs:
                yield int(crt([mp, mq], [p, q]))

import logging

# Some logging so we can see what's happening.
logging.basicConfig(level=logging.DEBUG)

n=57996511214023134147551927572747727074259762800050285360155793732008227782157
p=172036442175296373253148927105725488217
q=337117592532677714973555912658569668821
e=17
C=19441066986971115501070184268860318480501957407683654861466353590162062492971

possible_plaintexts = attack(n, e, (p-1)*(q-1), C)
for pt in possible_plaintexts:
    print(long_to_bytes(pt))
```

Run with `sage` and grepping all the possible plaintext messages for the correct flag.

```
sage -python attacks/rsa/non_coprime_exponent.py | grep 'dice{'
```

---

<details><summary>FLAG:</summary>

```
dice{cado-and-sage-say-hello}
```

</details>
<br/>
