#### Challenge:

Your crypto professor is back again! After having taught you some things about RSA, they have sprung another pop quiz. According to them, it is harder and longer. You should still be able to crack it, right? `nc crypto.chal.csaw.io 5008`

---

#### Solution:

This challenge was composed of `4` sub-challenges. All of them were different types of `RSA problems`. Let's go throuh them one by one:

1. This is one of the most common RSA attacks in CTFs!

    In this challenge we are provided with `N`, `e`, `C`. Interesting thing is that the `e` is comparable in size with `N`. From this I assumed that the solution would be `Wiener attack` and used [this library](https://github.com/pablocelayes/rsa-wiener-attack/blob/master/RSAwienerHacker.py).


    ```python
    from RSAwienerHacker import hack_RSA

    print(r.recvuntil("Part 1 --> This is one of the most common RSA attacks in CTFs!").decode('utf-8').strip())
    print(r.recvuntil("N = ").decode('utf-8').strip(), end=" ")
    N = int(r.recvline().decode('utf-8').strip())
    print(N)

    print(r.recvuntil("e = ").decode('utf-8').strip(), end=" ")
    e = int(r.recvline().decode('utf-8').strip())
    print(e)

    print(r.recvuntil("c = ").decode('utf-8').strip(), end=" ")
    c = int(r.recvline().decode('utf-8').strip())
    print(c)

    hacked_d = hack_RSA(e, N)
    print(hacked_d)
    plain_dec = pow(c, hacked_d, N)
    print("plain_dec")
    print(plain_dec)
    plain_str = binascii.unhexlify(hex(plain_dec)[2:])
    print(plain_str.decode('utf-8'))

    print(r.recvuntil("What is the plaintext?").decode('utf-8').strip())
    # r.sendline(plain_str.decode('utf-8'))
    r.sendline("Wiener wiener chicken dinner")
    ```

2. Sexy primes were used to make the modulus!

    In this challenge we are again given `N`, `e`, `C`. There was nothing special about them at first glance, so I just dumped them and manually run them through the [RsaCtfTool](https://github.com/Ganapati/RsaCtfTool). It turned out that the `N` was factorizable using `z3_solver` method.

    ```python
    print(r.recvuntil("Part 2 --> Sexy primes were used to make the modulus!").decode('utf-8').strip())
    print(r.recvuntil("N = ").decode('utf-8').strip(), end=" ")
    N = int(r.recvline().decode('utf-8').strip())
    print(N)

    print(r.recvuntil("e = ").decode('utf-8').strip(), end=" ")
    e = int(r.recvline().decode('utf-8').strip())
    print(e)

    print(r.recvuntil("c = ").decode('utf-8').strip(), end=" ")
    c = int(r.recvline().decode('utf-8').strip())
    print(c)

    ## Integer factorization using RsaCtfTool

    print(r.recvuntil("What is the plaintext?").decode('utf-8').strip())
    r.sendline("Who came up with this math term anyway?")
    ```

3. Looks like there is a oracle which is telling the LSB of the plaintext. That will not help you, right?

    In this one we get decrypting `oracle` that is leeking last bit of plaintext. Googlin about it leads us to [this](https://github.com/ashutosh1206/Crypton/tree/master/RSA-encryption/Attack-LSBit-Oracle) and [this](https://github.com/akalin/cryptopals-python3/blob/master/challenge46.py) repo, with that its easy to implement the following code:

    ```python
    print(r.recvuntil("Part 3 --> Looks like there is a oracle which is telling the LSB of the plaintext. That will not help you, right?").decode('utf-8').strip())
    print(r.recvuntil("N = ").decode('utf-8').strip(), end=" ")
    N = int(r.recvline().decode('utf-8').strip())
    print(N)

    print(r.recvuntil("e = ").decode('utf-8').strip(), end=" ")
    e = int(r.recvline().decode('utf-8').strip())
    print(e)

    print(r.recvuntil("c = ").decode('utf-8').strip(), end=" ")
    c = int(r.recvline().decode('utf-8').strip())
    print(c)
    print(r.recvuntil("What would you like to decrypt? (please respond with an integer)").decode('utf-8').strip())

    lower_limit = 0
    upper_limit = 1
    denominator = 1

    for i in range(1, N.bit_length()):
        chosen_ct = ((c*pow(2**i, e, N)) % N)
        r.sendline(str(chosen_ct))

        text = r.recvuntil("The oracle responds with: ").decode('utf-8').strip()
        lsb = int(r.recvline().decode('utf-8').strip())

        delta = upper_limit - lower_limit
        upper_limit *= 2
        lower_limit *= 2
        denominator *= 2

        if lsb == 0:
            upper_limit = upper_limit - delta
        elif lsb == 1:
            lower_limit = lower_limit + delta
        else:
            print("Error")
            exit(1)

        ask = r.recvuntil("Would you like to continue? (yes/no)").decode('utf-8').strip()
        r.sendline("yes")

    plain_str = long_to_bytes(upper_limit * N // denominator)

    ## One more turn to get out of the Oracle loop
    r.sendline(str(c))
    text = r.recvuntil("The oracle responds with: ").decode('utf-8').strip()
    print(text, end=" ")
    lsb = int(r.recvline().decode('utf-8').strip())
    print(lsb)
    print(r.recvuntil("Would you like to continue? (yes/no)").decode('utf-8').strip())
    r.sendline("no")

    print(r.recvuntil("What is the plaintext?").decode('utf-8').strip())
    # r.sendline(plain_str)
    r.sendline("Totally did not mean to put an oracle there")
    ```

4. Oops, looks like I leaked part of the private key. Hope that doesn't come back to bite me!

    In this last challenge we are given `N`, `e`, `c` and part of the private key (512 lower bits) as `d0`. Researching this I came across paper [Partial Key Exposure Attack
On Low-Exponent RSA](http://honors.cs.umd.edu/reports/lowexprsa.pdf) and [this implementation](https://gist.github.com/maojui/bd55d98d310bab770a6a0681078b444e). Using the python I dumped the challenge params:

    ``` python
    # print(r.recvuntil("Part 4 --> Oops, looks like I leaked part of the private key. Hope that doesn't come back to bite me!").decode('utf-8').strip())
    print(r.recvuntil("N = ").decode('utf-8').strip(), end=" ")
    N = int(r.recvline().decode('utf-8').strip())
    print(N)

    print(r.recvuntil("e = ").decode('utf-8').strip(), end=" ")
    e = int(r.recvline().decode('utf-8').strip())
    print(e)

    print(r.recvuntil("d0 = ").decode('utf-8').strip(), end=" ")
    d0 = int(r.recvline().decode('utf-8').strip())
    print(d0)

    print(r.recvuntil("c = ").decode('utf-8').strip(), end=" ")
    c = int(r.recvline().decode('utf-8').strip())
    print(c)

    print(r.recvuntil("d0bits = ").decode('utf-8').strip(), end=" ")
    d0bits = int(r.recvline().decode('utf-8').strip())
    print(d0bits)

    print(r.recvuntil("nBits = ").decode('utf-8').strip(), end=" ")
    nBits = int(r.recvline().decode('utf-8').strip())
    print(nBits)

    ## Dumped the parameters to solve this challenge in sage.

    print(r.recvuntil("What is the plaintext?").decode('utf-8').strip())
    r.sendline("I'll be careful next time to not leak the key")
    ```

    And then I modified the [sage script](https://gist.github.com/maojui/bd55d98d310bab770a6a0681078b444e) to crack the parameters for the last challenge:

    ```python
    from sage.all import *
    preparser(True)

    def partial_p(p0, kbits, n):
        PR.<x> = PolynomialRing(Zmod(n))
        nbits = n.nbits()

        f = 2^kbits*x + p0
        f = f.monic()
        roots = f.small_roots(X=1, beta=0.5)  # find root < 2^(nbits//2-kbits) with factor >= n^0.3
        if roots:
            x0 = roots[0]
            p = gcd(2^kbits*x0 + p0, n)
            return ZZ(p)

    def find_p(d0, kbits, e, n):
        X = var('X')

        for k in range(1, e+1):
            results = solve_mod([e*d0*X - k*X*(n-X+1) + k*n == X], 2^kbits)
            for x in results:
                p0 = ZZ(x[0])
                p = partial_p(p0, kbits, n)
                if p:
                    return p


    if __name__ == '__main__':
        n = 78632240941833807855884772524330065835402955795806709394355303103097021967177436509088552595566116542786074987330152184864206637790866313645184704053644088561487424230526088653911259055423031098715283509043278968205439924524516375373689799672629475846480810893265238820248309975880911531883397098125821250061
        e = 17
        d0 = 4502471974272025182526693403036719202327361476993820192384918494334957489065061713003663401342776185062816201807809117087380583099901561366552685815810697
        c = 61760213554270143562251462526047118626605361469303346790813136319254115478075166561147802493531635869359330073067722549268736982974343038474933596096140317352907894233771430758879194409657954937541315163889994043319781443228691310581676412579285155104637781053348918283872574145079753090878378971311498585637
        kbits = 512
        nBits = 1024

        beta = 0.5
        epsilon = beta^2/7

        nbits = 1024
        print("lower %d bits (of %d bits) is given" % (kbits, nbits))

        p = find_p(d0, kbits, e, n)
        print("found p: %d" % p)

        ## We have p, now get the plaintext
        import gmpy2
        from Crypto.Util.number import long_to_bytes

        q = n//p
        assert p*q == n
        d = gmpy2.invert(e, (p-1)*(q-1))
        pt = pow(c, d, n)
        print(long_to_bytes(pt).decode('utf-8'))
    ```

---

<details><summary>FLAG:</summary>

```
flag{l00K5_L1K3_y0u_H4v3_p4223D_7h3_D1ff1Cul7_r54_p0p_Kw12_w17H_fLy1N9_C0L0r2}
```

</details>
<br/>
