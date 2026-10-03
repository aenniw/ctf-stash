#### Challenge:

In the heart of the Misc Realm, R-Boy prepares for the decisive battle. He never expected to encounter an old foe: the master of the digital underworld in this realm is Zer0, someone he knows well. The atmosphere grows increasingly tense, and Zer0 reveals an ace up his sleeve: an extremely advanced Artificial Intelligence called "Nethra," programmed to predict and counter every move R-Boy makes. However, it seems that some clues for gaining an advantage have been disguised.

[http://gamebox1.reply.it/crypto1-f8dcb45c431202a866cf47e45be0dd44cc21cae0/](http://gamebox1.reply.it/crypto1-f8dcb45c431202a866cf47e45be0dd44cc21cae0/)

---

#### Solution:

The service hands me the public key `N`, `e`, the target ciphertext `C` (the encrypted flag), and an
`/oracle` endpoint that decrypts any ciphertext I send &mdash; except, of course, it won't just hand
back the flag for `C`. As the flag itself hints, textbook ("raw") RSA is
**multiplicatively homomorphic**:

```
Dec(c1 * c2 mod N) = Dec(c1) * Dec(c2) mod N
```

So I can blind the flag ciphertext past the oracle: pick a small plaintext `k = 2`, compute its
ciphertext `k^e mod N`, multiply it into `C`, and ask the oracle to decrypt the product. What comes
back is `k * flag mod N`; since `k * flag` is far smaller than `N` there is no modular wrap, so I just
divide by `k` to recover the flag and convert it to bytes:

```python
from gmpy2 import mpz
import binascii, requests

# N, e, C are published by the challenge
k = 2
tampered_ciphertext = (pow(k, e, N) * C) % N
r = requests.post(
    "http://gamebox1.reply.it/crypto1-<token>/oracle",
    json={"cipher": str(tampered_ciphertext)},
)
tampered_plaintext = int(r.text)          # == k * flag

flag_plaintext = tampered_plaintext // k  # undo the blinding
flag = binascii.unhexlify(mpz(flag_plaintext).digits(16))
print(flag)
```

The oracle call itself can't be re-run now (the `gamebox1.reply.it` host is long gone), but I kept the
`tampered_plaintext` the oracle returned during the event, and the final step &mdash;
`tampered_plaintext // 2` &rarr; hex &rarr; bytes &mdash; reproduces the flag exactly, confirming the
attack.

---

<details><summary>FLAG:</summary>

```
{FLG:H0mom0rf1c_Vu7N3R5b1liTi3s_0n_RSA_:)}
```

</details>
