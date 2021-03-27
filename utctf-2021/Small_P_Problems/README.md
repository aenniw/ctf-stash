#### Challenge:

My buddies Whitfield and Martin were trying to share a secret key between themselves, and I was able to eavesdrop on their conversation. I bet I could probably figure out their shared secret with a little math...

```text
p = 69691
g = 1001

A = 17016
B = 47643
```

**Note: submit either the shared secret or the shared secret wrapped in `utflag{}`**

---

#### Solution:

The challenge text points to `Diffie-Hellman` key exchange. Since all the numbers seem quite small, I decided to just brute force it.

```python
import gmpy2

p = 69691
g = 1001

A = 17016
B = 47643

a = 0
b = 0

for x in range(1000000000):
    if gmpy2.powmod(g, x, p) == A:
        a=x
        break
print(a)

s1 = gmpy2.powmod(B, a, p)
print("utflag{"+str(s1)+"}")
```

---

<details><summary>FLAG:</summary>

```text
utflag{53919}
```

</details>
<br/>
