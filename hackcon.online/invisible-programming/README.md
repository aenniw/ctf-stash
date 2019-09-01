#### Challenge:

Is this really a C program? [hello_world.cpp](./hello_world.cpp ':ignore')

---

#### Solution:

```python
#!/bin/python
import re

flag = ''

with open('./hello_world.cpp') as file:
    for line in file:
        quotes = False
        payload = ''

        if '}' in line:
            line = line.rstrip()

        if re.search('[a-zA-Z]', line):
            line = line.rstrip()
            line = line.lstrip()

        for ch in line:
            if ch == '"':
                quotes = not quotes
            if quotes:
                continue

            if ch == '\t':
                payload += '1'
            elif ch == ' ':
                payload += '0'

        if len(payload) > 0:
            flag += chr(int(payload, 2))

print(flag)

```

---

<details><summary>FLAG:</summary>

```
d4rk{L3t'5_hav3_50m3_fun_w1th_wh1te5pac35}c0de
```

</details>