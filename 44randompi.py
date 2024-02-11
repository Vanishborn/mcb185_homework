# 44randompi.py by Henry Li and Lisa Yuan

import random

in_circle = 0
in_square = 0

while True:
	x = random.random()
	y = random.random()

	if (x**2 + y**2) <= 1:
		in_circle += 1
		in_square += 1
	else:
		in_square += 1

	print(4*in_circle/in_square)
