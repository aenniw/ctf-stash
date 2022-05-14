#### Challenge:

Clam managed to get parole for his dumb cryptography jokes, but after making yet another dumb joke on his way out of the courtroom, he was sent straight back in. This time, he was sentenced to 5 years of making dumb Vigenere challenges. Clam, fed up with the monotony of challenge writing, made a program to do it for him. Can you solve enough challenges to get the flag?

Connect to the challenge at `nc challs.actf.co 31333`. [Source](./main.py ":ignore")

---

#### Solution:

We need to break several `Vigenere ciphers` by submitting fake `flegs` in order to get the actual flag. The `flegs` are padded with random strings of random length on both sides but luckily, we can see from the source that the `flegs` have standard flag prefix `actf{` and suffix `}fleg`, which we can use as `cribs`, and the keys have only the length of `4` chars so breaking them should be easy.

```python
#!/usr/bin/env python

from pwn import *
from struct import *
import string

r = remote('challs.actf.co', 31333)

alpha = string.ascii_lowercase

def encrypt(msg, key):
    ret = ""
    i = 0
    for c in msg:
        if c in alpha:
            # (position of cypher text char in alphabet + position of key char in alphabet) = char of alphabet
            ret += alpha[(alpha.index(key[i]) + alpha.index(c)) % len(alpha)]
            i = (i + 1) % 4
        else:
            ret += c
    return ret

def decrypt(msg, key):
    ret = ""
    i = 0
    for c in msg:
        if c in alpha:
            ret += alpha[(len(alpha) + alpha.index(c) - alpha.index(key[i])) % len(alpha)]
            i = (i + 1) % 4
        else:
            ret += c
    return ret


def get_key(crib_dec, crib_enc):
    key = ""
    i = 0
    for c in crib_enc:
        key += alpha[((len(alpha) + alpha.index(crib_enc[i])) - alpha.index(crib_dec[i])) % len(alpha)]
        i = (i + 1) % 4
    return key


# We know that key size is 4
# and we know that first 5 chars of plaintext are actf{ and last 5 chars are }fleg - cribs
# we also know that '{' and '}' are not being encrypted/decrypted
key_size=4

i = 0
while True:
    print(r.recvuntil(b": ").decode('utf-8').strip())
    challenge = r.recvline().decode('utf-8').strip()

    possible_start_cribs = re.findall('[a-z]{4}\{',challenge)
    possible_end_cribs = re.findall('\}[a-z]{4}',challenge)

    # print(possible_start_cribs)
    # print(possible_end_cribs)

    possible_start_keys = []
    for possible_start_crib in possible_start_cribs:
        possible_start_keys.append(get_key('actf',possible_start_crib[:-1]))

    possible_end_keys = []
    for possible_end_crib in possible_end_cribs:
        possible_end_keys.append(get_key('fleg',possible_end_crib[1:]))

    # print(possible_start_keys)
    # print(possible_end_keys)

    possible_keys = []
    for possible_start_key in possible_start_keys:
        for possible_end_key in possible_end_keys:
            for rot in range(key_size):
                a_list = collections.deque(possible_end_key)
                a_list.rotate(rot)
                shifted_end_key = "".join(a_list)
                # print(shifted_end_key)
                if possible_start_key == "".join(shifted_end_key):
                    for rot2 in range(key_size):
                        b_list = collections.deque(possible_start_key)
                        b_list.rotate(rot2)
                        possible_keys.append("".join(b_list))

    # print(possible_keys)

    possible_plains = []
    for possible_key in possible_keys:
        plain_with_noise = decrypt(challenge, possible_key)
        possible_plains.append(re.findall('actf\{.*\}fleg',plain_with_noise))

    plain = [x for x in possible_plains if x != []][0][0][:-key_size]

    if i % 50 == 49:
        print(plain)
        exit(1)

    r.sendline(plain)
    i += 1
```

---

<details><summary>FLAG:</summary>

```
actf{classical_crypto_is_not_the_best}
```

</details>
<br/>
