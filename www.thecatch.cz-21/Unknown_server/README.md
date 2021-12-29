#### Challenge:

Hi Expert,

the archaeologist have found strange server on IP `78.128.246.144`. Although it replies to ping, no services are present. Check the purpose of the server. 

Good Luck!

---

#### Solution:

- inspecting the `ping` request from server reveals hint `Send ICMP type 8 code 0 and Epoch time in payload`, after sending crafted `ping` the flag is revealed

```python
from pythonping import ping
import time

ping('78.128.246.144', verbose=True, payload=str(int(time.time())))
```

---

<details><summary>FLAG:</summary>

```
FLAG{4c7J-hehJ-wIOY-BAx2}
```

</details>
<br/>
