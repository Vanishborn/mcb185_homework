# 56birthday.py by Henry Li

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

def has_duplicates(my_list):
	seen = []
	for item in my_list:
		if item in seen:
			return True
		seen.append(item)
	return False

count = 0

for i in range(trials):
	birthday_list = []

	for j in range(people):
		birthday_list.append(random.randint(1, days))

	if has_duplicates(birthday_list):
		count += 1

print(f"{(count / trials * 100):.2f}%")
