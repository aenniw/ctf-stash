#### Challenge:

Hi, junior investigator!

We have wiretaped strange communication - probably a message. Try to decode it. [wiretaped_message.tar.xz](./wiretaped_message.tar.xz ":ignore")

Good Luck!

---

#### Solution:

```python
#!/bin/python3

import struct
import base64
import re

def find_flag_in_string(string):
    regex = r"FLAG\{.{4}-.{4}-.{4}-.{4}\}"
    matches = re.findall(regex,string)
    return matches

with open("message", "rb") as file_handle:
    while True:
        try:
            # Convert first two bytes to int (Big endian)
            length = int(struct.unpack('>h', file_handle.read(2))[0])

            # Read and print message
            message = base64.b64decode(file_handle.read(length)).decode('utf-8')
            # print(message)

            flag = find_flag_in_string(message)
            if flag:
                print(flag)
        except:
            print("Error or EOF")
            break;
```

---

<details><summary>FLAG:</summary>

```
FLAG{YHsB-hr0J-W2ol-fV17}
```

</details>
<br/>
