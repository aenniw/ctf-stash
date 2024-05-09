#### Challenge:

Hi Commander,

did you know that the berserkers, which were assigned to specific tasks, have used to name themselves after humans famous in given field of specialization (this behaviour is maybe some bug in their firmware)? Our infiltrators - remotely operated classic devices equiped with stickers `I'm smart` and `Death to humans` - have discovered a new Berserker named `Colonel Roche`, which is responsible for encrypting the commands for the other less or more smart devices. Your previous successes obviously forced the Berserkers to improve the security of communication. You are supposed to find some way how to decrypt a captured message and read the issued command(s). The infiltrators report that this particular machine usually uses a day of week as a key (maybe `monday`, maybe `saturday`, maybe something else... they are not sure).

Good luck! [colonel_roche.encrypted.gz](./colonel_roche.encrypted.gz ":ignore")

---

#### Solution:

- based on [TheCatch-18 - The Colonel](/www.thecatch.cz-18/round-2-leaked/README?id=the-colonel)

```python
#!/usr/bin/env python2

import sys


def get_pos(p):
    return ord(p.lower()) - 96


def normalize(keys):
    min = 255
    sorted = keys[:]
    sorted.sort()
    normalized = []
    for k in keys:
        normalized.append(sorted.index(k) + 1)

    return normalized


def decrypt(data, key):
    keys = []
    for k in key:
        keys.append(get_pos(k))

    keys = normalize(keys)

    table = []
    data_count = 0
    for l in range(0, len(key)):
        line = []
        for r in range(0, len(key)):
            line.append('')
        table.append(line)

    for r in range(0, len(key)):
        for l in range(0, len(key)):
            if keys[r] >= 1:
                table[l][r] = data[data_count]
                data_count += 1
                keys[r] -= 1

    encoded = []
    for l in range(0, len(key)):
        for r in range(0, len(key)):
            encoded.append(table[l][r])

    return "".join(encoded)


def split(x, p):
    chunks, chunk_size = len(x), p
    return [x[i:i+chunk_size] for i in range(0, chunks, chunk_size)]


if __name__ == "__main__":
    secret = '463216327617246f67406f1266075ec622606c6671765537066636596e621e64e622c2b006066961c66e621f067676e77c6e665167a462c4b50477433617754222d7043542885747df6dd575970417d435223000'

    keys = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    for i in range(1, 168):
        parts = split(secret, len(secret)/i)
        for k in keys:
            decr = ""
            for p in parts:
                try:
                    decr = decr + decrypt(p, k)
                except:
                    pass
            if decr != '':
                try:
                    flag = decr.decode('hex')
                    if 'FLAG' in flag:
                        print(k + ' -> ' + flag)
                except:
                    pass
```

---

<details><summary>FLAG:</summary>

```
FLAG{uB8W-XBtp-OmtE-Q2Ys}
```

</details>
