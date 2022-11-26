#### Challenge:

Hi, packet inspector,

our company uses on-board route recorders, so traffic controller can optimize movement of all vehicles and also control the schedule. Any route can be described by a text string that contains the codes of individual sites in the order in which they were visited (except depot, because each drive starts and also ends there).

Unfortunately, one of the recorders has been damaged and the particular sites were not recorded, just the total length of the route is known (exactly `163 912 meters`). In addition, the driver told us that he never visited the same place more than once (except depot, of course).

Your task is to identify the exact route of the vehicle.

Download [the map of vehicle operating area and backround info](./route_tracking.zip ":ignore") (MD5 checksum `5fd3f52bcb404eae543eba68d7f4bb0a`).

May the Packet be with you!

---

#### Solution:

In this challenge we have to find specific path in the graph. It reminded me [one of the older challenges](../../challenges.reply.com-21/aMazing_Super_Power/README.md). So I took the solution script from it and bent it a little to solve this one. The [sites.txt](./sites.txt) and [distances.txt](./distances.txt) were created manually from the `DOT` file for my convenience.

```python
#!/usr/bin/env python

import copy

# Get the list of the sites with codes
sites={}
with open('sites.txt') as f:
    lines = f.readlines()
    for line in lines:
        site_data = line.strip().split("=")
        sites[site_data[0]] = site_data[1]


# Get the connection between sites and their distances
pairs = []
table = {}
with open('distances.txt') as f:
    lines = f.readlines()
    for line in lines:
        pair_data = line.strip().replace('-','&').replace('=','&').replace(',','&').split('&')
        pairs.append(pair_data)
        table[pair_data[0]+pair_data[1]] = [pair_data[2]]
print(table)


def get_cities_after(path):
    global SHORTEST_TIME
    global FINAL_PATH

    remaining_cities = list(set_cities - set(path['cities']))

    possible_next_cities = []
    for city in remaining_cities:
        if (path['cities'][-1]+city) in table.keys():
            possible_next_cities.append(city)

    for city in possible_next_cities:
            distance = path['distance'] + int(table[path['cities'][-1]+city][0])

            if (distance <= 163912):
                newpath = copy.deepcopy(path)
                newpath['distance'] = distance
                newpath['cities'].append(city)

                if (len(newpath['cities']) == 26 and city != '025'):
                    return
                elif (len(newpath['cities']) == 26):
                    new_distance = newpath['distance'] + int(table[newpath['cities'][-1]+newpath['cities'][0]][0])

                    if (new_distance == 163912):
                        finishpath = copy.deepcopy(newpath)
                        finishpath['distance'] = new_distance
                        finishpath['cities'].append(path['cities'][0])
                        FINAL_PATH = finishpath
                        print(newpath)

                get_cities_after(newpath)

def myFunc(e):
  return e[0]

pairs.sort(key=myFunc)

cities = []
for pair in pairs:
    if pair[0] not in cities:
        cities.append(pair[0])

print(cities)
print(len(cities))

set_cities = set(cities)
PATHS = []
FINAL_PATH = {}
path = {
    'time_spent': 0,
    'distance': 0,
    'cities': ['000']
}
get_cities_after(path)

# Get FLAG by traversing the final path
cities = ""
for city in FINAL_PATH['cities']:
    cities = cities + sites[city]

password = str(cities + "-" + str(FINAL_PATH['distance']))
print(password)
```

---

<details><summary>FLAG:</summary>

```
FLAG{SLiH-QPWV-hIm5-hWcU}
```

</details>
<br/>
