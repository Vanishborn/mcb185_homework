# 71countgff.py by Henry Li

import sys
import gzip

count = {}

with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		if line.startswith('#'):
			continue
		f = line.split()
		feature = f[2]
		if feature not in count:
			count[feature] = 0
		count[feature] += 1

		# if feature not in count:
		# 	count[feature] = 1
		# else:
		# 	count[feature] += 1

# for f, n in count.items():
# 	print(f, n)

# for k in sorted(count):
# 	print(k, count[k])

for k, v in sorted(count.items(), key=lambda item: item[1]):
	print(k, v)
