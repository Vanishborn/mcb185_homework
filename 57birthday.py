# 57birthday.py by Henry Li

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

def has_duplicated_days(my_list):
	for n in my_list:
		if n > 1:
			return True
	return False

count = 0

for i in range(trials):
	calendar = []

	for j in range(365):
		calendar.append(0)

	for k in range(people):
		calendar[random.randint(0,364)] += 1

	if has_duplicated_days(calendar):
		count += 1

print(f"{(count / trials * 100):.2f}%")
