#### Challenge:

Alice and Bob are back to sending and receiving encrypted  messages again, and this time <i>you</i> can be part of  the conversation! <br><br> <b>Download the file below and open the <code>Deployment</code> tab to start this challenge.</b> [server.py](./server.py ":ignore")

---

#### Solution:

We are given `Python` source code to the messaging server. When the server starts it encrypts the flag using `RSA` with the private key that we don't have. But we are able to `encrypt` any message (how many times we want) and `decrypt` any message `once` (because of receive pinning, which also prevents us to decrypt the flag directly as it is also pinned). This leads us to chose RSA [Self-reducibility Attack](https://people.csail.mit.edu/rivest/RivestKaliski-RSAProblem.pdf).:

We know that the flag's plaintext `m` was `encrypted` to ciphertext `c` using classic textbook RSA:

<center><img src="https://render.githubusercontent.com/render/math?math=c = m^e ( mod N )"></center>

And we know the `decryption` process with private key `d` (which we don't have) looks like this:

<center><img src="https://render.githubusercontent.com/render/math?math=m = c^d ( mod N )"></center>

Now to the `attack` part. If we choose appropriate plaintext `m'` let's say `m' = 2` and encrypt it we get (chosen) ciphertext `c'`:

<center><img src="https://render.githubusercontent.com/render/math?math=c^' = {m^'}^e ( mod N )"></center>

Now we compute tampered ciphertext `c''` by multiplying the original flag's ciphertext with our chosen ciphertext:

<center><img src="https://render.githubusercontent.com/render/math?math=c^'' = c * c^' ( mod N )"></center>

And use the server to decrypt it to get tampered plaintext `m''`:

<center><img src="https://render.githubusercontent.com/render/math?math=m^'' = {c^''}^d ( mod N )"></center>

Using the equations above:

<center><img src="https://render.githubusercontent.com/render/math?math=m^'' = (c * c^') ^d ( mod N )"></center>

<center><img src="https://render.githubusercontent.com/render/math?math=m^'' = (c^d)* ({c^'}^d)( mod N )"></center>

<center><img src="https://render.githubusercontent.com/render/math?math=m^'' = m* m^' ( mod N )"></center>

Now we want to solve for:

<center><img src="https://render.githubusercontent.com/render/math?math=m = m^''/ m^' ( mod N )"></center>

If we set for `m'`  the original chosen value `2` we ("undo the tampering" and) get original flag's plaintext `m`:

<center><img src="https://render.githubusercontent.com/render/math?math=m = m^''/ 2 ( mod N )"></center>


```python
#!/usr/bin/env python3

from pwn import *
from gmpy2 import *
import binascii

global s

try:
    s = remote('challenge.ctf.games', 31029)
    try:
        ## Get flag
        print(s.recvuntil('Ciphertext: ').decode())
        flag_ciphertext = int(s.recvline().decode()[:-1])
        print(flag_ciphertext)

        ## Get public key
        payload='KEY:'
        s.sendline(payload)
        print(payload)
        N=int(s.recvline().decode()[2:-1])
        print("N:"+str(N))
        e=int(s.recvline().decode()[2:-1])
        print("e:"+str(e))

        # Choose chosen_plaintext create chosen_ciphertext and tampered_ciphertext
        chosen_plaintext=2
        chosen_ciphertext = chosen_plaintext**e % N
        tampered_ciphertext = (chosen_ciphertext * flag_ciphertext) % N

        # Send tamperred ciphertext for decryption
        payload='RECV:'+str(tampered_ciphertext)
        s.sendline(payload)
        print(payload)
        s.recvline()

        # Get tampered_plaintext
        tampered_plaintext=int(s.recvline().decode()[:-1])
        print("tampered_plaintext:"+str(tampered_plaintext))

        # Extract flag_plaintext from tampered_plaintext by dividing by chosen_plaintext:
        flag_plaintext = int(tampered_plaintext) // int(chosen_plaintext)
        print("flag_plaintext:"+str(flag_plaintext))

        # Convert base10 binary message to base16 string
        flag_hex_string_without_0x = mpz(flag_plaintext).digits(16)
        print("flag_hex_string_without_0x:"+str(flag_hex_string_without_0x))

        # Convert every 2 binary message characters from base 16 to one string character
        flag = binascii.unhexlify(flag_hex_string_without_0x)
        print(flag)

    finally:
        s.close()
except Exception as e:
    raise
```

---

<details><summary>FLAG:</summary>

```
flag{schoolhouse_crypto_with_our_favorite_characters}
```

</details>
<br/>
