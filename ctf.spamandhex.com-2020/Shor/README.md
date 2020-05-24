#### Challenge:

I've successfully built a quantum computer and now I want to factor RSA keys to show the world just how unsecure those are. I'm a bit stuck with the classical part of Shor's algorithm, please help me. Here are my partial results after running the quantum part:

[file_1.txt](./file_1.txt ":include :type=code")

[file_2.txt](./file_2.txt ":include :type=code")

[file_3.txt](./file_3.txt ":include :type=code")

---

#### Solution:

The challenge hints to Shor's algorithm, which is designed to factor large primes using quantum computers. We are given the outputs of the quantum steps, so only thing we need to do, is the implementation. Quick Google search returns resources like [Wikipedia](https://en.wikipedia.org/wiki/Shor%27s_algorithm) or [MathGradBlog](https://blogs.ams.org/mathgradblog/2014/04/30/shors-algorithm-breaking-rsa-encryption/) based on these we were able to write the algorithm, but we only decrypted the first message which reveals only part of the flag - `SaF{Wikipedia_still`. After a day of desperation and futile attempts to factor the remaining public keys by conventional methods, I came across the article [Shor’s Algorithm and Factoring:
Don’t Throw Away the Odd Orders](https://eprint.iacr.org/2017/083.pdf), which says that we don't need to throw away `odd orders` as the original Shor's algorithm directed, we just need to factor them, try to use their factors instead of the order, in the original algorithm. This reveals the factors of the public key and enables us to decrypt the whole message.

```python
#!/env python3


from secrets import randbits, randbelow
from sympy import nextprime
from sympy.ntheory.modular import crt
from Crypto.Util.number import long_to_bytes
import math
import gmpy2
import codecs

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
import sympy.ntheory as nt

######
# https://eprint.iacr.org/2017/083.pdf
##
# Testcases:
#    recycle_quantum_findings(751228, 78, 3304283)
#    recycle_quantum_findings(2, 4247705, 152942113)
#


def recycle_quantum_findings(a, s, N):

    r = 1
    tactical_divisor = 1

    # while we still haven't found what we are looking for
    while tactical_divisor == 1:

        print(f"trying factor of order: {r}")
        reminder = 1
        quotient = s

        # find new perfect quotient
        while reminder != 0:
            print(f"no dice {r}, lets find next prime")
            r = nt.nextprime(r)
            (quotient, reminder) = gmpy2.t_divmod(s, r)

        br = gmpy2.powmod(a, quotient, N)
        tactical_divisor = gmpy2.gcd(br - 1, N)

    print("tactical divisor:")
    print(tactical_divisor)

    tactical_divisor2 = N // tactical_divisor
    print("tactical divisor2:")
    print(tactical_divisor2)

    assert tactical_divisor * tactical_divisor2 == N

    return (tactical_divisor, tactical_divisor2)


# cycle through the files with the inputs
for i in range(1, 4):
    file = open("file_"+str(i)+".txt", "r")

    print("######## Starting with f"+str(i)+".txt")

    N = gmpy2.mpz(file.readline().split('=')[1].strip())
    e = gmpy2.mpz(file.readline().split('=')[1].strip())
    message = gmpy2.mpz(file.readline().split('=')[1].strip())
    base_element = gmpy2.mpz(file.readline().split('=')[1].strip())
    order_of_base = gmpy2.mpz(file.readline().split('=')[1].strip())

    # Shor's algorithm - classical parts:
    # https://blogs.ams.org/mathgradblog/2014/04/30/shors-algorithm-breaking-rsa-encryption/
    # https://en.wikipedia.org/wiki/Shor%27s_algorithm
    ##

    # Step 1.
    if gmpy2.gcd(base_element, N) == 1:
        print("######## No usefull GCD can be easily found, lets try some magic...")
    else:
        print("######## Nontrivial GCD - EZ life. Skipping")
        continue

    # Step 2 is quantum, I don't have HW for that shit... Yet...
    # Luckily we are already provided with P from the quantum computer owner.

    # Step 3 - check odd / even
    (quotient, reminder) = gmpy2.t_divmod(order_of_base, 2)
    if (reminder == 0):
        # order is not odd we can continue

        # Step 4
        b = gmpy2.powmod(base_element, quotient, N)
        if b != (N - 1):
            # period was not trivial we can get p,q continue clasically:
            p = gmpy2.gcd(b + 1, N)
            q = gmpy2.gcd(b - 1, N)
        else:
            # maximumm effort
            (p, q) = recycle_quantum_findings(base_element, order_of_base, N)

    else:
        # maximumm effort
        (p, q) = recycle_quantum_findings(base_element, order_of_base, N)

    # sanity check
    assert p*q == N

    print("######## p:")
    print(p)
    print("######## q:")
    print(q)

    # Decipher RSA
    # STEP Create private key 'd'

    phi_n = (p-1) * (q-1)
    d = gmpy2.invert(gmpy2.mpz(e), gmpy2.mpz(phi_n))

    # sanity check
    x = gmpy2.mul(gmpy2.mpz(d), gmpy2.mpz(e))
    assert gmpy2.t_mod(x, gmpy2.mpz(phi_n)) == 1

    # STEP decipher 'message' to 'plain'
    plain = gmpy2.powmod(gmpy2.mpz(message), gmpy2.mpz(d), gmpy2.mpz(N))

    print("######## plain")
    print(hex(plain)[2:])
    print(codecs.decode(hex(plain)[2:], 'hex'))

```

```
python3 shor.py | grep -o -e '\".*\"' | tr -d '"\n'
```

---

<details><summary>FLAG:</summary>

```
SaF{Wikipedia_still_says_you_have_to_discard_odd_orders...}
```

</details>
<br/>
