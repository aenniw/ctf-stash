#### Challenge:

I made a function

```python
def func(bits):
	keys = gen_rsa_key(bits)
	p = keys.p
	q = keys.q
	m = getPrime(bits+1)
	x = pow(p, m, m)*pow(q, m, m) + p*pow(q, m, m) + q*pow(p, m, m) + p*q + pow(p, m-1, m)*pow(q, m-1, m)
	text = os.urandom(32)
	print('Plaintext (b64encoded) : ', b64encode(text).decode())
	print()
	print(hex(x)[2:])
	print(hex(m)[2:])
	# print(b64encode(encrypt(keys, text)))
	print()
	ciphertext = input('Ciphertext (b64encoded) : ')
	check()
```
Can you help me encrypt some data with this :) `nc crypto.byteband.it 7001`

---

#### Solution:

```bash
```

---

<details><summary>FLAG:</summary>

```

```

</details>
<br/>
