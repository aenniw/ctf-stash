#### Challenge:

Follow the [crumbs](https://crumbs.web.actf.co).

Server: [index.js](./index.js ":ignore")

---

#### Solution:

We follow a chain of url slugs. Each slug either gives us a different slug to follow prefixed with "Go to " or the flag text.

```py
#! /usr/bin/python3

import requests

valid_flag = False
flag = ""
slug = ""
base_url = "https://crumbs.web.actf.co/"
while not valid_flag:
    curr_url = base_url + slug
    r = requests.get(url = curr_url)
    print(i)
    if "Go to " in r.text:
        slug = r.text[6:]
    else:
        valid_flag = True
        flag = r.text
print(flag)
```
```
actf{w4ke_up_to_th3_m0on_6bdc10d7c6d5}
```

---

<details><summary>FLAG:</summary>

```
actf{w4ke_up_to_th3_m0on_6bdc10d7c6d5}
```

</details>
<br/>
