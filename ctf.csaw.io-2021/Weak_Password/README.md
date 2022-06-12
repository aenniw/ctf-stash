#### Challenge:

Can you crack Aaron’s password hash? He seems to like simple passwords. I’m sure he’ll use his name and birthday in it. Hint: Aaron writes important dates as YYYYMMDD rather than YYYY-MM-DD or any other special character separator. Once you crack the password, prepend it with `flag{` and append it with `}` to submit the flag with our standard format. Hash: `7f4986da7d7b52fa81f98278e6ec9dcb`.

---

#### Solution:

We know from the challange description that the password will have format `AaronYYYYMMDD`. Creating a simple script to try every single day since `1900-01-01` and comparing the `MD5` hash with the one provided was fairly easy.

```python
import datetime
import hashlib

crack_hash = '7f4986da7d7b52fa81f98278e6ec9dcb'


day = datetime.datetime(1900,1,1)
hash = hashlib.md5('Aaron'+day.strftime("%Y%m%d"))

while hash.hexdigest() != crack_hash:
    day = day + datetime.timedelta(days=1)
    hash = hashlib.md5('Aaron'+day.strftime("%Y%m%d"))
    print(hash.hexdigest())
    print('Aaron'+day.strftime("%Y%m%d"))

print('Aaron'+day.strftime("%Y%m%d"))
```

---

<details><summary>FLAG:</summary>

```
flag{Aaron19800321}
```

</details>
<br/>
