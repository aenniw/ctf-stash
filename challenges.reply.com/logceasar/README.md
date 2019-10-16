#### Challenge:

The satellite communications have stopped working – suddenly they're sending back unknown algorithms. Help R-boy decipher them.
[encrypted.txt](./encrypted.txt ":ignore") [encrypt.py](./encrypt.py ":ignore")

---

#### Solution:

```python
#!/usr/bin/env python3
import sys


def decrypt(message, key):
    with open(message, 'rb') as content_file:
        content = content_file.read()
    if len(content) != 256:
        raise Exception(
            'This is a block cipher, messages have to be exactly 256 bytes long (%d)' % len(content))
    ciphertext = list(' ' * 256)
    for i in range(0, 256):
        new_pos = (3**(key+i)) % 257
        ciphertext[i] = ((content[new_pos-1]) ^ i) ^ (new_pos-1)
    return bytes(ciphertext)


plaintext = decrypt(sys.argv[1], int(sys.argv[2]))
with open(sys.argv[3], 'wb') as encryped_file:
    encryped_file.write(plaintext)
```

```bash
mkdir decrypts
for i in `seq 0 256`; do
    ./decrypt.py encrypted.txt $i ./decrypts/decrypt-$i.txt;
done
cat $(grep 'FLG' ./decrypts/* | awk '{print $5}')
```

---

<details><summary>FLAG:</summary>

```
{FLG:but_1_th0ught_Dlog_wa5_h4rd}
```

</details>
