#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyproj
import matplotlib.pyplot as plt
import LatLon as latlon
import numpy as np



with open('targets.txt','r') as f:
    lines = f.readlines()
f.closed

x_vals = np.array([])
y_vals = np.array([])

for coord in lines:
    lat,lon = coord.split(', ')

    lalo = latlon.string2latlon(lat.strip(),lon.strip(),'d% %m%\'%S%"%H')
    x1,y1 = lalo.to_string('D')

    x_vals = np.append(x_vals, float(x1))
    y_vals = np.append(y_vals, float(y1))



plt.plot(y_vals, x_vals)
plt.show()