#### Challenge:

Clam decided to return to classic cryptography and revisit the XOR cipher! Here's some hex encoded ciphertext:

```text
ae27eb3a148c3cf031079921ea3315cd27eb7d02882bf724169921eb3a469920e07d0b883bf63c018869a5090e8868e331078a68ec2e468c2bf13b1d9a20ea0208882de12e398c2df60211852deb021f823dda35079b2dda25099f35ab7d218227e17d0a982bee7d098368f13503cd27f135039f68e62f1f9d3cea7c
```

The key is 5 bytes long and the flag is somewhere in the message.

---

#### Solution:

We have hex encoded ciphertext, we know the key is 5 bytes long and we know there is a flag, so essentially we know there is a `crib` - the flag prefix - `actf{`, which is also 5 bytes long, so we can get all possible keys by XOR-ing the crib with each group of 5 consecutive bytes of the ciphertext and then brute-force through these keys. The brute-force is feasible because the ciphertext has only `124 bytes` (248 hex characters) so there are 120 (124-5+1) consecutive groups of 5 characters = 120 possible keys.

```python
#!/bin/python3

import binascii

def repeat_string(a_string, target_length):
    number_of_repeats = target_length // len(a_string) + 1
    a_string_repeated = a_string * number_of_repeats
    a_string_repeated_to_target = a_string_repeated[:target_length]
    return a_string_repeated_to_target


def decipher_vernam(ciphertext_bytes, key_bytes):
    # expand key
    repeated_key_bytes = repeat_string(key_bytes, len(ciphertext_bytes))
    try:
        result = bytes(a ^ b for (a, b) in zip(ciphertext_bytes, repeated_key_bytes)).decode()
        print(result)
    except:
        print("Could not decode")


ciphertext_bytes = bytearray.fromhex("ae27eb3a148c3cf031079921ea3315cd27eb7d02882bf724169921eb3a469920e07d0b883bf63c018869a5090e8868e331078a68ec2e468c2bf13b1d9a20ea0208882de12e398c2df60211852deb021f823dda35079b2dda25099f35ab7d218227e17d0a982bee7d098368f13503cd27f135039f68e62f1f9d3cea7c")
krib_ascii = "actf{"

krib_bytes =  bytearray.fromhex(krib_ascii.encode("utf-8").hex())
repeated_crib_bytes = repeat_string(krib_bytes, len(ciphertext_bytes))
key_material = bytes(a ^ b for (a, b) in zip(ciphertext_bytes, repeated_crib_bytes))

for i in range(len(key_material)):
    possible_key = key_material[i:i+len(krib_ascii)]
    print(f"Trying key: {possible_key}")
    decipher_vernam(ciphertext_bytes, possible_key)
```

```bash
python3 solve.py | grep " actf{"
```

---

<details><summary>FLAG:</summary>

```text
actf{who_needs_aes_when_you_have_xor}
```

</details>
<br/>
