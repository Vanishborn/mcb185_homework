# 33triples.py by Henry Li and Lisa Yuan

# for i in range(1, 100):
# 	for j in range(1, 100):
# 		for k in range(1, 200):
# 			if i**2 + j**2 == k**2 and i <= j:
# 				print(i, j, k)

# another way

import math

def is_perfect_square(n):
	root = math.sqrt(n)
	if math.isclose(root, root // 1):
		return True
	return False

for i in range(1, 100):
	for j in range(1, 100):
		if is_perfect_square(i**2 + j**2) and i <= j:
			print(i, j, int(math.sqrt(i**2 + j**2)))
