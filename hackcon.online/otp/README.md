#### Challenge:

hackerman is so dank that he decided to play around with OTPs.
he did the following:
message1 ^ key = cipher1
message2 ^ key = cipher2

He gives you cipher1 and cipher2 and challenges you to find the concatenation of messages 1 and 2.
Are you dank enough to find this?
Oh and also, 'meme' is so popular that hackerman used the word in both his messages.
cipher1 is '\x05F\x17\x12\x14\x18\x01\x0c\x0b4'
cipher2 is '>\x1f\x00\x14\n\x08\x07Q\n\x0e'
Both without quotes

---

#### Solution:

```python
'd4rk{?????' ^ key = cipher1 => 'd4rk{' ^ key[:-5] = cipher1[:-5]
'?????}c0de' ^ key = cipher2 => '}c0de' ^ key[5:] = cipher2 [5:]
```

```python
from pwn import *;

cipher1 = '\x05F\x17\x12\x14\x18\x01\x0c\x0b4'
cipher2 = '>\x1f\x00\x14\n\x08\x07Q\n\x0e'

key = xor(cipher1[:-5], 'd4rk{') + xor(cipher2[-5:], '}c0de')
print(xor(cipher1, key) + xor(cipher2, key))
```

---

<details><summary>FLAG:</summary>

```
d4rk{meme__meme}c0de
```

</details>
