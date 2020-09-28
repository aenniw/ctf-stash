#### Challenge:

Bob asked Alice to make the keys easier to guess. She did it but to keep the data safe, she used two keys and encrypted the data twice. Can you prove that she is absolutely wrong by getting the flag? [output.txt](./output.txt ":ignore"), [source.py](./source.py ":ignore")

---

#### Solution:

The text file that we are given contains one plaintext/ciphertext pair and ciphertext of the flag. The python source code that we are given shows that the plaintext is encrypted once with the first half of the key and then the ciphertext is encrypted again with the second half of the key. This (and also the name of the challenge) leads us to use `Meet in the middle` attack. The challenge creators we also good to us by defining the key:

The first half is defined as (where # is unknown `printable` character):

```
"0000000000000###"
```

The second half is defined as (where # is unknown `printable` character):

```
"###0000000000000"
```

So although both halves of the key have 16 bytes each, we "only" need to bruteforce `6 printable characters` (100^6 possibilities) which is still not feasible. Luckily this amount is further reduced by meet-in-the-middle attack because we only need to create `rainbow table` with `middle values` (all possible ciphertexts for original plaintext encrypted using all possible first-half keys) for `3 printable characters` and then start generating middle values by decrypting original ciphertext using all possible second-half keys and looking them up in the rainbow table. (So the resulting possibilities needed to be tried are somewhere between `(100^3 ; 2*(100^3)>` which doable. When we get a hit we know we have the `correct key` and can decrypt the encrypted flag.

```python
#!/usr/bin/python

import random
from Crypto.Cipher import AES
from os import urandom
from string import printable

import binascii


from Crypto.Cipher import AES
plain = 'aaaaaaaaaaaaaaaa'.encode('hex')
cipher = 'ef92fab38516aa95fdc53c2eb7e8fe1d5e12288fdc9d026e30469f38ca87c305ef92fab38516aa95fdc53c2eb7e8fe1d5e12288fdc9d026e30469f38ca87c305'.decode('hex')
unknown = 'fa364f11360cef2550bd9426948af22919f8bdf4903ee561ba3d9b9c7daba4e759268b5b5b4ea2589af3cf4abe6f9ae7e33c84e73a9c1630a25752ad2a984abfbbfaca24f7c0b4313e87e396f2bf5ae56ee99bb03c2ffdf67072e1dc98f9ef691db700d73f85f57ebd84f5c1711a28d1a50787d6e1b5e726bc50db5a3694f576'.decode('hex')

KEY_PADDING = '0'*13

def NewAES(key):
  return AES.new(key, mode=AES.MODE_ECB)

def Encrypt(short_key, text=plain):
  return NewAES(KEY_PADDING+short_key).encrypt(text)

def Decrypt(short_key, text=cipher):
  return NewAES(short_key+KEY_PADDING).decrypt(text)

def Decrypt1(short_key, text=cipher):
  return NewAES(KEY_PADDING+short_key).decrypt(text)

def KeyGen1():
  """Generator for all possible 24 bit keys."""
  for a in printable:
    for b in printable:
      for c in printable:
        yield ''+a+''+b+''+c+''

def KeyGen2():
  """Generator for all possible 24 bit keys."""
  for d in printable:
    for e in printable:
      for f in printable:
        yield ''+d+''+e+''+f+''

def RainbowTable():
  """Map of encryptions to keys."""
  table = {}
  for short_key in KeyGen1():
    table[Encrypt(short_key, plain).encode('hex')] = short_key
  return table

rainbow_table = RainbowTable()
for short_key in KeyGen2():
  decrypted = Decrypt(short_key, cipher)
  if decrypted in rainbow_table:
    # Have a match, now decrypt the flag
    print(short_key)
    print("XXXXX")
    print(rainbow_table[decrypted])
    ct1 = Decrypt(short_key, unknown).decode('hex')
    result = Decrypt1(rainbow_table[decrypted],ct1).decode('hex')
    print(result)
    break
```

---

<details><summary>FLAG:</summary>

```
flag{y0u_m@d3_i7_t0_7h3_m1dddl3}
```

</details>
<br/>
