# 45dndstats.py by Henry Li and Lisa Yuan

import random

sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0

# assuming number of rolls to 1Mil times
rolls = 1000000

for i in range(rolls):
	value1 = 0
	value2 = 0
	value3 = 0
	value4 = 0

	# rule 1: 3D6
	for j in range(3):
		roll = random.randint(1, 6)
		value1 += roll
	sum1 += value1

	# rule 2: 3D6r1
	for j in range(3):
		roll = random.randint(1, 6)
		if roll == 1:
			roll = random.randint(1, 6)
		value2 += roll
	sum2 += value2

	# rule 3: 3D6x2
	for j in range(3):
		roll1 = random.randint(1, 6)
		roll2 = random.randint(1, 6)
		if roll1 > roll2:
			roll = roll1
		else:
			roll = roll2
		value3 += roll
	sum3 += value3

	# rule 4: 4D6d1
	lowest = 6
	for j in range(4):
		roll = random.randint(1, 6)
		if roll < lowest:
			lowest = roll
		value4 += roll
	sum4 += value4 - lowest

avg1 = sum1 / rolls
avg2 = sum2 / rolls
avg3 = sum3 / rolls
avg4 = sum4 / rolls

print(f'3D6:\t{avg1}\n3D6r1:\t{avg2}\n3D6x2:\t{avg3}\n4D6d1:\t{avg4}')
