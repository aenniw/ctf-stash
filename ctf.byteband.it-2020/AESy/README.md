#### Challenge:

Alice made an encryption service for Bob to encrypt his messages and to leave encrypted messages for her. Can you use this service to find the flag?

`nc crypto.byteband.it 7004`

---

#### Solution:

The service provides useful three actions:

1. Get your message encrypted.
2. Leave a message for Alice to decrypt.
3. Get Encrypted Flag.

The first action gets us ciphertext for chosen plain text.

The second action lets us submit a ciphertext to Alice. Based on the ciphertext submitted she will return different responses:

  - `Alice: Got your message!!` - the ciphertext is valid
  - `Alice: Got your message??` - the IV was tampered with
  - `Alice: You have just given me the IV. There is no encrypted message appended to it??` - only `IV` was submitted
  - `Alice: There are non-hex digits in the ciphertext.` - the ciphertext was tampered with
  - `Alice: Ciphertext length is not a multiple of block length(=16).` - the ciphertext was tampered with

The third option gets us the ciphertext of the flag (for every session the `IV` is regenerated so the flag has to be decrypted in one session.)

With the above knowledge I created test function for the padding oracle attack and after letting it run long enough I got the flag.

```python
#!/usr/bin/env python3

from pwn import *
import padding_oracle
import json
from Crypto.Cipher import AES

global s

def oracle(data):
    print("[*] Trying: {}".format(data.hex()))

    s.sendline('2')
    ciphertext_prompt = s.recvuntil('Enter the ciphertext(hex-encoded):\n').decode()

    # Send automatically tampered ciphertext
    s.sendline(data.hex())
    resp = s.recvuntil('Enter your choice:\n').decode()

    # Return response from oracle based on validity of tampered ciphertext
    if 'Alice: Got your message!!' in resp:
        print("!!!HIT!!!")
        return True
    else:
        return False
    # elif   'Alice: Got your message..??' in resp \
    #     or 'Alice: You have just given me the IV. There is no encrypted message appended to it??' in resp \
    #     or 'Alice: There are non-hex digits in the ciphertext.' in resp \
    #     or 'Alice: Ciphertext length is not a multiple of block length(=16).' in resp:
    #         return False

if __name__ == '__main__':
    try:
        s = remote('crypto.byteband.it', 7004)
        try:
            ## GET FLAG
            print(s.recvuntil('Enter your choice:\n').decode())
            s.sendline('3')

            print(s.recvuntil('Here is your ciphertext(hex-encoded):\n').decode())
            encrypted_flag = s.recvline().decode().strip()
            print(encrypted_flag)

            cipher = bytes.fromhex(encrypted_flag)
            print(cipher.hex())

            ## Run Padding Oracle Attack
            plaintext = padding_oracle.padding_oracle(cipher, block_size=16, oracle=oracle, num_threads=1)

            print("plaintext:", plaintext)
            print(plaintext)

            print(s.recvuntil('Enter your choice:\n').decode())

        finally:
            s.close()
    except Exception as e:
        raise
```

---

<details><summary>FLAG:</summary>

```
flag{th3_0racl3_0nly_gu1de$_7he_1337}
```

</details>
<br/>
