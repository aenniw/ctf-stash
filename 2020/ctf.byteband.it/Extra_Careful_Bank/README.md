#### Challenge:

the Extra Careful Bank claims to have the greatest encryption for its transactions. it is so sure no one can forge the encrypted transactions that it is going to process any valid encrypted transactions.
Can you get the flag?

`nc crypto.byteband.it 7003`

---

#### Solution:

We start with `10$`. Playing around the application we figured that after `10 transactions` we get more options.

The advanced options are following:

- See today's transactions(encrypted)
  - Lists last 20 ciphertexts
- See special transaction(encrypted)
  - Returns one transaction with ammount of `500$`
- Provide encrypted transactions.
  - Boasts that if we provide 3 valid transaction ciphertexts they will be performed.
- Get flag.
  - Gets us flag for the cost of `1500$`

Trying to randomly provide ciphertext we get following response in error:

```text
Transaction Format:
sender account number(16 bytes)+receiver account number(16 bytes)+amount(prepended appropriately to 16 bytes)
```

So we know how the transaction ciphertext is built. Trying random entries from the `todays transactions` we can `get our ID` by picking a random transaction, swapping sender block with the receiver block, performing it and checking our balance. If its non-zero we reverted one of the transactions from the first 10 that unlocked the advanced options menu for us.

The next step is to scan special transaction option for 3 different transactions. This way we get two things - we get the block that represents `500$` amount and 3 receiver IDs that accepted `500$` transactions (so we can essentially rob them :D ).

Next step is to craft and perform the 3 encrypted transaction because we have 3 sender ID blocks, we know our ID block for receiver and we know amount block for `500$`.

Only thing left is to buy the flag.

```python
#!/usr/bin/env python3

from pwn import *

try:
    s = remote('crypto.byteband.it', 7003)

    try:
        print(s.recvuntil('Enter your choice:\n').decode())

        # get to the advanced menu after 10 transactions
        for i in range(10):
            s.sendline('1')
            print(s.recvuntil('Enter the receiver id(1, 2 or 3):\n').decode())
            s.sendline('1')
            print(s.recvuntil('Enter amount(min = $1, max = $500):\n').decode())
            s.sendline('1')
        print(s.recvuntil('Enter your choice:\n').decode())

        # get todays transactions to get your own ID
        s.sendline('2')
        todays_transactions_raw = s.recvuntil('Enter your choice:\n').decode()
        todays_transactions = todays_transactions_raw.split('\n')[:20]
        fake_trans = ""
        for trans in todays_transactions:
            fake_trans = trans[32:64]+trans[:32]+trans[64:]
            print(trans)
            print(fake_trans)
            s.sendline('4')
            print(s.recvuntil('First encrypted transaction:\n').decode())
            s.sendline(fake_trans)
            print(s.recvuntil('Second encrypted transaction:\n').decode())
            s.sendline('')
            print(s.recvuntil('Third encrypted transaction:\n').decode())
            s.sendline('')

            print(s.recvuntil("BALANCE: $").decode())
            balance = s.recvline().decode().strip()
            print(balance)
            print(s.recvuntil('Enter your choice:\n').decode())
            if balance != "0":
                break

        my_id = fake_trans[32:64]
        bill_500 = ""
        receivers = []

        while len(receivers) < 3:
            s.sendline('3')
            print(s.recvuntil('This is an encrypted transaction involving a transfer of $500:\n').decode())
            transaction = s.recvline().decode().strip()
            bill_500 = transaction[64:]
            if transaction[32:64] not in receivers:
                receivers.append(transaction[32:64])

            print(s.recvuntil('Enter your choice:\n').decode())
        print(receivers)

        s.sendline('4')
        for receiver in receivers:
            fake_trans = receiver + my_id + bill_500
            print(s.recvuntil('encrypted transaction:\n').decode())
            s.sendline(fake_trans)

        print(s.recvuntil('Enter your choice:\n').decode())
        s.sendline('5')
        print(s.recvuntil('Enter your choice:\n').decode())


    finally:
      s.close()

except Exception as e:
    raise
```

---

<details><summary>FLAG:</summary>

```
flag{bank$_sh0uld_n07_us3_ECB}
```

</details>
<br/>
