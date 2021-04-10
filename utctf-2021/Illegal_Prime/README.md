#### Challenge:

The NSA published the ciphertext from a one-time-pad. Since breaking one-time-pad is so easy, I did it for you.

To avoid legal trouble I can't tell you the key. On an unrelated note I found this really cool [prime number](https://en.wikipedia.org/wiki/Illegal_prime).

[challenge.txt](./challenge.txt ":ignore")

---

#### Solution:

After Googling for Illegal primes (prime numbers that represent program or file possession of which is not legal) I found this [writeup](https://github.com/shiltemann/CTF-writeups-public/blob/master/Hackvent_2016/writeup.md#dec-9-illegal-prime-number).

```python
#!/usr/bin/python2
import binascii

p  = 56594044391339477686029513026021974392498922525513994709310909529135745009448534622250639333011770158535778535848522177601610597930145120019374953248865595853915254057748042248348224821499113613633807994411737092129239655022633988633736058693251230631716531822464530907151
p2 = binascii.unhexlify(hex(p)[2:-1])
p3 = bytearray(p2)

with open("output",'w') as outfile:
    outfile.write(p2)
```

After running the modified code, I found out that the output is simple text file containing the one-time-pad key. Using [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')XOR(%7B'option':'Hex','string':'5a0b05d9831438ac8561d2b0a42be1cf5613db21deb9a443e21c4d'%7D,'Standard',false)&input=MmY3ZjYzYjVlMjczNDNkY2Y3NTBiZjgzZmI0ODkzZmUzYjIwYTg3ZTgxZTZmYjYyYzMzZDMw) I deciphered the flag.

---

<details><summary>FLAG:</summary>

```text
utflag{pr1m3_cr1m3s____!!!}
```

</details>
<br/>
