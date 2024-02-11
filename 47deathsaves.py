# 47deathsaves.py by Henry Li and Lisa Yuan

import random

# assuming 1Mil rolls
rolls = 1000000

dead = 0
stablelized = 0
revived = 0

for i in range(rolls):
	succ = 0
	fail = 0
	while True:
		roll = random.randint(1, 20)
		if roll == 20:
			revived += 1
			break
		elif roll == 1:
			fail += 2
			if fail >= 3:
				dead += 1
				break
		elif roll >= 10:
			succ += 1
			if succ == 3:
				stablelized += 1
				break
		else:
			fail += 1
			if fail == 3:
				dead += 1
				break

avg_dead = dead / rolls
avg_stbl = stablelized / rolls
avg_revi = revived / rolls

print(
	f'|  Dead  |  Stablelized  |  Revived  |\n|:------:|:------:|:------:|\n|{avg_dead}|{avg_stbl}|{avg_revi}|')
