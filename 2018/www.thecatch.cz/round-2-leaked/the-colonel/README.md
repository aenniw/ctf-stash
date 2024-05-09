#### Challenge:

Agent, we have intercepted a message send by foreign agent "Colonel" to his headquarter and it has to be deciphered. Our profiling team has discovered, that the nickname "Colonel" come from his obsession of the cipher used by some colonel in 19th century, probably named "Roche". Furthermore, he always choose day of the week as the cipher key. Let's hurry, Agent! `48024325d765d74677381378554d2c650d5380073602407d94440000`

---

#### Solution:

```python
import sys

def get_pos(p):
	return ord(p.lower()) - 96

def normalize(keys):
	min = 255
	sorted =  keys[:]
	sorted.sort()
	normalized = []
	for k in keys:
		normalized.append(sorted.index(k) + 1)

	return normalized


def encrypt(data,key):
	keys = []
	for k in key:
		keys.append(get_pos(k))

	keys = normalize(keys)

	table = []
	data_count = 0
	for l in range(0, len(key)):
		line = []
		for r in range(0, len(key)):
			if keys[r] >= 1:
				if(data_count >= len(data)):
					line.append('+')
				else:
					line.append(data[data_count])
				data_count += 1
				keys[r] -= 1
			else:
				line.append('')
		table.append(line)

	coded = []
	for l in range(0, len(key)):
		for r in range(0, len(key)):
			coded.append(table[r][l])

	return "".join(coded)

def decrypt(data, key):
	keys = []
	for k in key:
		keys.append(get_pos(k))

	keys = normalize(keys)

	table = []
	data_count = 0
	for l in range(0, len(key)):
		line = []
		for r in range(0, len(key)):
			line.append('')
		table.append(line)

	for r in range(0, len(key)):
		for l in range(0, len(key)):
			if keys[r] >= 1:
				table[l][r] = data[data_count]
				data_count += 1
				keys[r] -= 1

	encoded = []
	for l in range(0, len(key)):
		for r in range(0, len(key)):
			encoded.append(table[l][r])


	return "".join(encoded)

if __name__ == "__main__":
	print decrypt(sys.argv[1], sys.argv[2])
```

```bash
declare -a arr=("Tuesday")

for i in "${arr[@]}"
do
   python Roche.py "48024325d765d74677381378554d" "$i"  | xxd -r -p
   python Roche.py "2c650d5380073602407d94440000" "$i"  | xxd -r -p
done
```

---

<details><summary>FLAG:</summary>

```
CT18-hpWx-uGVM-pyLS-F6DX
```

</details>
