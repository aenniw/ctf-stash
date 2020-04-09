#### Challenge:

Agent, we need your skills! Foreign blonde agent Pamela forgot her laptop in the café and our agency got it. Unfortunately, all user files are encrypted with something called `Advanced_Quantum_Prediction_Mk3` and we are not able to break it. However, Pamela has used an encryption application `Agency Secure Communicator` in the debug mode, which could leave useful traces. Analyse the event log and try to find some messages in plain text if possible. Good luck, Agent. [asc.evtx](./asc.evtx ":ignore")

---

#### Solution:

Inspecting the provided Windows event log file reveals two types of data sets:
- One with debug message `Message chunk saved` which contains essentially two columns of data (base64 encoded):
   
    1. `position of the character in the plaintext message` 
    2. `cryptext string representing one plaintext character`    

- The second type of data payload (base64 encoded) with debug message `Chunk encryption performed` contains:
   
    1. `cryptext string representing one plaintext character`
    2. `plaintext character` (decimal ASCII value)

We perform `(inner) join` over these two data sets based on `cryptext string representing one plaintext character` and print `plaintext character`s `ordered by` the `position of the character in the plaintext message` and get the resulting message (again base64 encoded).

```python
#!/bin/env python3
# -*- coding: UTF-8 -*-

## pip install python-evtx
## pip install bs4
## pip install lxml

from bs4 import BeautifulSoup
import Evtx.Evtx as evtx
import base64
import re

DEBUG=False
order_cryptstring_tuple_list = []
cryptstring_plainchar_tuple_list = []

with evtx.Evtx('asc.evtx') as log:
    for record in log.records():
        bs = BeautifulSoup(record.xml(), "lxml")
        if DEBUG:
            print(bs.prettify())

        if "Message chunk saved" in str(bs.find('data').text):
            if DEBUG:
                print(str(base64.b64decode(str(bs.find('binary').text))))

            id_enc_pair = re.search(r'chunkid="([0-9]*)";encrypted="([A-Z]*)"', str(base64.b64decode(str(bs.find('binary').text))))
            if id_enc_pair and id_enc_pair.group(1) and id_enc_pair.group(2):
                order_cryptstring_tuple_list.append((int(id_enc_pair.group(1)), str(id_enc_pair.group(2))))

        elif "Chunk encryption performed" in str(bs.find('data').text):
            if DEBUG:
                print(str(base64.b64decode(str(bs.find('binary').text))))

            id_dec_pair = re.search(r'plain="([0-9]*)";encrypted="([A-Z]*)"', str(base64.b64decode(str(bs.find('binary').text))))
            if id_dec_pair and id_dec_pair.group(1) and id_dec_pair.group(2):
                cryptstring_plainchar_tuple_list.append((str(id_dec_pair.group(2)), int(id_dec_pair.group(1))))

if DEBUG:
    print(order_cryptstring_tuple_list)
    print(cryptstring_plainchar_tuple_list)

plaintext = ""
for order, cryptstring_FK in order_cryptstring_tuple_list:
    for cryptstring_PK, plainchar in cryptstring_plainchar_tuple_list:
        if cryptstring_FK == cryptstring_PK:
            plaintext = plaintext + chr(int(plainchar))
            break

print(base64.b64decode(plaintext))
```

---

<details><summary>FLAG:</summary>

```
CT18-QnTK-50Uq-vQ5o-jAS5
```

</details>
