# 43randomdna.py by Henry Li and Lisa Yuan

import random

num_seq = 3

for i in range(1, num_seq+1):
	print(f'>seq-{i}')
	length = random.randint(50, 60)
	for j in range(length):
		print(random.choice('ACGT'), end='')
	print('')
