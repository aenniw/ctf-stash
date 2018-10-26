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
		# 	print table[l][r] if len(table[l][r]) > 0 else '_',
		# print


	return "".join(encoded)

class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg


coded = encrypt(data,key)
print coded
print decrypt(coded,key)
print data

# CT18-hpWx-uGVM-pyLS-F6DX

if __name__ == "__main__":
	print decrypt(sys.argv[1], sys.argv[2])