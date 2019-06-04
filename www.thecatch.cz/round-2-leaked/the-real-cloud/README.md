#### Challenge:

Agent, you have been assigned a new task. Thanks to our network monitoring probes we have detected a flood of ICMP packets. The purpose of these packets remains unknown. The sad news is that the packets were originating from our internal network! It appears there is a mole in our agency. Do not panic, everything is under control - we will find the double agent and he/she will be brought to fair justice. You are to inspect these packets. If you find any sensitive data, report to us immediately! Godspeed, Agent. PS: In _completely unrelated_ news - agent Maulwurf's status is KIA. Any more information is highly classified. [capture.zip](./capture.zip ':ignore')

---

#### Solution:

```python
from pcapng import FileScanner
from pcapng.blocks import *
from pcapng.utils import *
import numpy as np

prev = []
with open('capture.pcapng', 'rb') as fp:
    scanner = FileScanner(fp)
    for block in scanner:
      if type(block) is SectionHeader or \
         type(block) is InterfaceDescription:
         continue
      elif  type(block) is EnhancedPacket:
        if np.array_equal(prev, block):
          continue
        print block.packet_data
      else:
        print type(block)
```

---

<details><summary>FLAG:</summary>

```
CT18-s8G7-o8Ks-0YUX-3feT
```

</details>
