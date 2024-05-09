#### Challenge:

Clam's tired of the drab life of being a Python programmer. When he heard of the legendary ginkoid coding in Go, he knew it was his calling. Before embarking on his dangerous journey to becoming a Google shill, he encrypted his most valued flag the only way he knows how: pure randomness. It's a good thing he did, too, since Google sold all his data for 2 cents and caused him to forget the flag. Can you recover his flag?

[Source](./dist.go ":ignore"), [Output](./chall.txt ":ignore")

---

#### Solution:

We are given `Go` source code in which the `32 byte flag` is divided into four `8-byte (64-bit)` chunks which are `XOR`-ed with `4` `consecutive` randomly generated `64-bit` numbers that are part of the sequence defined by unknown seed. We know resulting `64-bit` numbers of the `XOR`s and `607` `non-consecutive` `64-bit` random numbers that are also part of the same sequence and were generated `after` the `XORs`.

Googling the `go`'s `math/rand` library I found out that it is not cryptographically secure. I also found this nice [writeup](https://blog.cryptohack.org/bls-signatures-secret-rng-donjon-ctf-writeup) explaining `rand/math`'s functioning (so I will skip it here) and also providing the `Pseudo-Random Number Generator (PRNG)` reconstruction in Python. Since our situation differs in the fact that we know the numbers that were generated `after` the numbers we need to get the flag, I inverted the functions `next` and `set_next` to get `prev` and `set_prev`. With those functions then I used the provided numbers to reconstruct the `PRNG` state `going backwards` in time (or more precisely in the generated `PRNG` sequence).
With that, I was able to get the original numbers that the flag was encrypted with and decrypt the flag.


```python
#!/usr/bin/env python

# Read the challenge output file
chall_file = open('chall.txt', 'r')

# Read encrypted flag numbers
FLAG_NUMBERS=[]
for i in range(4):
    FLAG_NUMBERS.append(int(chall_file.readline().strip().replace("flag chunk: ","")))

# print(FLAG_NUMBERS)


# Read the known PRNG numbers from the challenge output file while adding "UNKNOWN constant to indicate gap
NUMBERS=[]
gap = 0
for i in range(607):
    ## Read known number
    NUMBERS.append(int(chall_file.readline().strip().replace("flag chunk: ","")))
    for j in range(gap):
        ## Append "UNKNOWN" to array to account for the gap
        NUMBERS.append("UNKNOWN")

    gap = (gap + 1) % 13

# print(NUMBERS)

chall_file.close()


# Go's PRNG representation in Python
# Static init values from https://github.com/golang/go/blob/d09ca2cb8ec5306f20b527266ce161bd9292cad4/src/math/rand/rng.go#L15
LEN = 607
TAP = 273
class Rng:
    def __init__(self):
        # Seed init values from https://github.com/golang/go/blob/d09ca2cb8ec5306f20b527266ce161bd9292cad4/src/math/rand/rng.go#L206
        # We don't need to set them, because we are going to work from the provided random numbers BACKWARDS to set the state
        self.vec = [0] * LEN
        self.tap = 0
        self.feed = LEN - TAP

    # Not really needed, just as reference to construct `set_next` and `prev`
    def next(self):
        self.tap -= 1
        if self.tap < 0:
            self.tap = LEN - 1
        self.feed -= 1
        if self.feed < 0:
            self.feed = LEN - 1
        if self.vec[self.feed] == "UNKNOWN" or self.vec[self.tap] == "UNKNOWN":
            self.vec[self.feed] ="UNKNOWN"
        else:
            self.vec[self.feed] = (self.vec[self.feed] + self.vec[self.tap]) % (2**64)
        return self.vec[self.feed]

    # Not really needed, just as reference to construct `set_prev`
    def set_next(self, val):
        self.tap -= 1
        if self.tap < 0:
            self.tap = LEN - 1
        self.feed -= 1
        if self.feed < 0:
            self.feed = LEN - 1
        self.vec[self.feed] = val

    # Get previous random number if known
    def prev(self):
        self.tap += 1
        if self.tap > LEN - 1:
            self.tap = 0
        self.feed += 1
        if self.feed > LEN - 1:
            self.feed = 0
        if self.vec[self.feed] == "UNKNOWN" or self.vec[self.tap] == "UNKNOWN":
            self.vec[self.feed] ="UNKNOWN"
        else:
            if (self.vec[self.feed] - self.vec[self.tap]) < 0:
                self.vec[self.feed] = ((2**64) + (self.vec[self.feed] - self.vec[self.tap])) % (2**64)
            else:
                self.vec[self.feed] = (self.vec[self.feed] - self.vec[self.tap])
        return self.vec[self.feed]

    # Set previous random number if next (and corresponding tap) are known
    def set_prev(self, val):
        self.tap += 1
        if self.tap > LEN - 1:
            self.tap = 0
        self.feed += 1
        if self.feed > LEN - 1:
            self.feed = 0
        if val != "UNKNOWN":
            self.vec[self.feed] = val
        else:
            if (self.vec[self.feed] - self.vec[self.tap]) < 0:
                self.vec[self.feed] = ((2**64) + (self.vec[self.feed] - self.vec[self.tap])) % (2**64)
            else:
                self.vec[self.feed] = (self.vec[self.feed] - self.vec[self.tap])

            if self.vec[self.feed] != "UNKNOWN":
                # print("We have set up something we didn't know before")
                pass

rng = Rng()

# Recreate the RNG state by working backwards on number we know
for i in range(len(NUMBERS)-1, 0, -1):
    rng.set_prev(NUMBERS[i])

# Last prev before flag should not be set_prev because we would overwrite the flag one,
# but we need to call it to adjust the `feed` and `tap` pointers
# print("Last prev (from backwards PoV) before the flag")
last_prev = rng.prev()
# print(last_prev)

# We are going backwards through NUMBER and FLAG_NUMBERS
reverse_flag = []
for flag_chunk in FLAG_NUMBERS[::-1]:
    original_rnd = rng.prev()
    result = original_rnd ^ flag_chunk
    reverse_flag.append(result.to_bytes(8,'little'))

# reverse the reverse and join the chunks
for flag_chunk in reverse_flag[::-1]:
    print(flag_chunk.decode("utf-8"), end="")
print()
```

---

<details><summary>FLAG:</summary>

```
actf{i_c4n_f0rs33_th3_p4s7_t00_}
```

</details>
<br/>
