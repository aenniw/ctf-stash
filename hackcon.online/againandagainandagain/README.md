#### Challenge:

Someone was thinking encrypting again and again helps, prove them wrong.

```
c = 196353764385075548782571270052469419021844481625366305056739966550926484027148967165867708531585849658610359148759560853
```
Edit: the flag format is slightly different [q1.py](./q1.py ':ignore')

---

#### Solution:

```python
#!/bin/pyhton


def xgcd(a, b):
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return x0, y0


def modular_sqrt(a, p):
    if legendre_symbol(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return 0
    elif p % 4 == 3:
        return pow(a, (p + 1) / 4, p)

    s = p - 1
    e = 0
    while s % 2 == 0:
        s /= 2
        e += 1

    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1

    x = pow(a, (s + 1) / 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e

    while True:
        t = b
        m = 0
        for m in xrange(r):
            if t == 1:
                break
            t = pow(t, 2, p)

        if m == 0:
            return x

        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m


def legendre_symbol(a, p):
    ls = pow(a, (p - 1) / 2, p)
    return -1 if ls == p - 1 else ls


def decrypt(m):
    mp = modular_sqrt(m, p)
    mq = modular_sqrt(m, q)

    yp, yq = xgcd(p, q)

    r1 = (yp * p * mq + yq * q * mp) % n
    r2 = n - r1
    r3 = (yp * p * mq - yq * q * mp) % n
    r4 = n - r3

    return (r1, r2, r3, r4)


def encrypt(m):
    return pow(m, 2, n)


def check_candidates(candidates):
    for c in candidates:
        try:
            text = hex(c).split('L')[0][2:].decode('hex')
            print(text)
            if 'd4rk' in text:
                return True
        except:
            pass
    return False


candidates = [
    196353764385075548782571270052469419021844481625366305056739966550926484027148967165867708531585849658610359148759560853]

p = 5411451825594838998340467286736301586172550389366579819551237
q = 5190863621109915362542582192103708448607732254433829935869841
n = p*q

while not check_candidates(candidates):
    new_candidates = []
    for c in candidates:
        for nc in decrypt(c):
            if nc not in new_candidates:
                new_candidates.append(nc)
    candidates = new_candidates

```

---

<details><summary>FLAG:</summary>

```
d4rk{r3p3t1t1v3_r4b1n_1s_th4_w0rs7_3vaaaaaar!}code
```

</details>
