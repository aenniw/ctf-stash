#### Challenge:

After an open battle, and thanks to the super strength of IronCode, R-Boy manages to get hold of the file. But it’s a trap. IronCode and R-boy are stuck into the file and the only way to get out is through a labyrinth of codes! Solve the problems in the maze and help the two heroes escape! [coding300.zip](./coding300.zip ":ignore")

---

#### Solution:

This challenge is standard coding challenge focusing on finding shortest path in the graph but it is made a bit more difficult by introducing few special conditions, like the paths have two dimensional "costs" - `time` and `energy`, also you can visit a specific node only in specific "time range". These conditions are in itself a good things, because they significantly reduce the number of permutations. Also recursion is the only way how to compute this in reasonable time. After finding the correct path, it provides us with the password to the `ZIP` archive containing the flag.

```python
#!/usr/bin/env python

import copy

def get_cities_before(path):
    global PATHS

    for city in cities:
        if city not in path['cities']:
            time_spent = path['time_spent'] + int(table[city+path['cities'][-1]][0])
            energy_spent = path['energy_spent'] + int(table[city+path['cities'][-1]][1])
            
            if (time_spent < 650 and energy_spent < 58000):

                newpath = copy.deepcopy(path)
                # print(newpath)
                newpath['time_spent'] = time_spent
                newpath['energy_spent'] = energy_spent
                newpath['cities'].append(city)

                PATHS.append(newpath)

                get_cities_before(newpath)
    

def get_cities_after(path):
    global SHORTEST_TIME
    global FINAL_PATH

    remaining_cities = list(set_cities - set(path['cities']))
    for city in remaining_cities:
            time_spent = path['time_spent'] + int(table[path['cities'][-1]+city][0])
            energy_spent = path['energy_spent'] + int(table[path['cities'][-1]+city][1])
            
            if (energy_spent <= 58000 and time_spent < SHORTEST_TIME):
                newpath = copy.deepcopy(path)
                newpath['time_spent'] = time_spent
                newpath['energy_spent'] = energy_spent
                newpath['cities'].append(city)

                if (len(newpath['cities']) == 14):
                    # Go from last city to first
                    new_time_spent = newpath['time_spent'] + int(table[newpath['cities'][-1]+newpath['cities'][0]][0])
                    new_energy_spent = newpath['energy_spent'] + int(table[newpath['cities'][-1]+newpath['cities'][0]][1])
                    
                    if (new_energy_spent <= 58000 and new_time_spent < SHORTEST_TIME):
                        finishpath = copy.deepcopy(newpath)
                        finishpath['time_spent'] = new_time_spent
                        finishpath['energy_spent'] = new_energy_spent
                        finishpath['cities'].append(path['cities'][0])
                        FINAL_PATH = finishpath
                        SHORTEST_TIME = new_time_spent

                get_cities_after(newpath)


# Read the file with the city pair data
with open('file.txt') as f:
    lines = f.readlines()

pairs = []
table = {}
for line in lines:
    pair_data = line.strip().replace('-','&').replace('=','&').replace(',','&').split('&')
    pairs.append(pair_data)
    table[pair_data[0]+pair_data[1]] = [pair_data[2], pair_data[3]]


# Build cities list (unique)
def myFunc(e):
  return e[0]

pairs.sort(key=myFunc)

cities = []
for pair in pairs:
    if pair[0] not in cities:
        cities.append(pair[0])

# print(cities)
# print(len(cities))

PATHS = []
path = {
    'time_spent': 0,
    'energy_spent': 0,
    'cities': ["Diagon Alley"]
}

get_cities_before(path)

HALF_PATHS = []
for path in PATHS:
    if path['time_spent'] > 135:
        path_reversed = copy.deepcopy(path)
        path_reversed['cities'] = copy.deepcopy(path['cities'][::-1])
        HALF_PATHS.append(path_reversed)

# Build cities list (unique)
def sortHalfPaths(item):
  return len(item['cities'])

HALF_PATHS.sort(key=sortHalfPaths)
set_cities = set(cities)

# Take all the paths up until Diagonal Valley and finish them up
SHORTEST_TIME = 999999999999999999999999999999
FINAL_PATH = {}
for path in HALF_PATHS:
    get_cities_after(path)   

# Get password for the final path
cities = ""
for city in FINAL_PATH['cities']:
    cities = cities + city[:2]

password = str(FINAL_PATH['time_spent']) + "-" + cities + "-" + str(FINAL_PATH['energy_spent'])
print(password)
```

---

<details><summary>FLAG:</summary>

```
{FLG:Wh47_sup3R_p0w3r_d0_J00_w4nt7}
```

</details>
