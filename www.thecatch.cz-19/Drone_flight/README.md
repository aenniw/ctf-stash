#### Challenge:

Hi Commander,

we have intercepted a message, which has been addressed to a rebellious supersonic drone in laboratory of one famous Czech university and it contains `B-1084 START`. The drone has already taken off and now it is beening monitored by our ground radar network. The achieved GPS coordinates have been recorded down, but it looks like purely random flight. You have to analyse the coordinates and find the hidden sense of this activity.

Good luck! [drone_flight.gps.gz](./drone_flight.gps.gz ":ignore")

---

#### Solution:

- based on [TheCatch-18 - The targets](/www.thecatch.cz-18/round-2-leaked/README?id=the-targets)
- note: use `python2` because at the time of writing `LatLon` library for `python3` does not exist

```bash
#!/usr/bin/env python2
# -*- coding: utf-8 -*-

## pip install matplotlib LatLon numpy

import matplotlib.pyplot as plt
import LatLon as latlon
import numpy as np

with open('drone_flight.gps','r') as f:
    lines = f.readlines()
f.closed

x_values = np.array([])
y_values = np.array([])
x2,y2 = 0,0
offset=0.0
for coord in lines:
    lat,lon = coord.split(', ')
    lalo = latlon.string2latlon(lat.strip(),lon.strip(),'d%°%m%\'%S%"%H')
    x1,y1 = lalo.to_string('D')


    if ((abs(float(y1)-float(y2))) > 200):
        plt.plot(y_values, x_values)
        x_values = np.array([])
        y_values = np.array([])
        offset=float(x2)

    x1=float(x1)+float(offset)
    x_values = np.append(x_values, float(x1))
    y_values = np.append(y_values, float(y1))

    x2,y2 = x1,y1

plt.plot(y_values, x_values)
plt.show()
```

---

<details><summary>FLAG:</summary>

```
FLAG{70Q3-d8yW-9aeT-VZIV}
```

</details>
