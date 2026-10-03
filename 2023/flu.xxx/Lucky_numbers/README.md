#### Challenge:

Help me to find my lucky numbers. Bad luck is around... `nc flu.xxx 10010``

[Download challenge files](./lucky.zip ":ignore")

---

#### Solution:

The service encrypts the flag with AES-CBC, prints the ciphertext, and then offers to decrypt it
for me &mdash; but only if I can tell it its two "lucky numbers" `s` and `t`. Reading
`lucky_number.py`, the checks on my two inputs are:

```python
if s<random.randrange(10000,20000):      ...  # s must be >= ~20000
if s>random.randrange(150000000000,200000000000): ... # s must be <= ~1.5e11
if t>42: ...                              # t <= 42
n=2**t-1
for i in range(2,int(n**0.5)+1):
    if (n%i)==0: ...                      # 2**t - 1 must be PRIME  (Mersenne prime -> t is a Mersenne exponent)
u=t-1
number=(2**u)*(2**(t)-1)                  # Euclid-Euler form of an EVEN PERFECT NUMBER
...                                        # A = all proper divisors of s
total=sum(A)
if total==s==number:                      # s must equal its proper-divisor sum AND equal `number`
    # ...decrypts and prints the flag
```

So the puzzle is pure number theory:

- `t` must be a **Mersenne prime exponent** (so that `2**t - 1` is prime): `t in {2,3,5,7,13,17,19,31}` within the `t<=42` limit.
- `number = 2**(t-1) * (2**t - 1)` is then an **even perfect number** (Euclid&ndash;Euler theorem), and the final check `total==s==number` demands that `s` be exactly that perfect number (its proper divisors sum to itself).
- `s` must also sit in `[~20000, ~1.5e11]`. The perfect numbers in that window are `33550336` (`t=13`), `8589869056` (`t=17`) and `137438691328` (`t=19`).

I pick `t=13` (fittingly, "Friday the 13th") and the perfect number `s = 2**12 * (2**13 - 1) = 33550336`:

```bash
# first prompt = s (the perfect number), second prompt = t (its Mersenne exponent)
{ echo 33550336; echo 13; } | nc flu.xxx 10010
# ...
# You found them, well done! Here have something for your efforts:
# flag{...}
```

I verified this against the provided `lucky_number.py` locally (with a dummy `FLAG`), and feeding
`33550336` / `13` makes it decrypt and print the flag.

---

<details><summary>FLAG:</summary>

```
flag{luck_0n_fr1d4y_th3_13th?}
```

</details>
