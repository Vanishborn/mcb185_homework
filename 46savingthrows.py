# 46savingthrows.py by Henry Li and Lisa Yuan

import random

# assuming 1Mil rolls
rolls = 1000000

suc5 = 0
suc10 = 0
suc15 = 0

suc_a5 = 0
suc_a10 = 0
suc_a15 = 0

suc_d5 = 0
suc_d10 = 0
suc_d15 = 0

for i in range(rolls):
	roll = random.randint(1, 20)
	if roll >= 5:
		suc5 += 1
	if roll >= 10:
		suc10 += 1
	if roll >= 15:
		suc15 += 1

for i in range(rolls):
	roll1 = random.randint(1, 20)
	roll2 = random.randint(1, 20)
	if roll1 > roll2:
		roll = roll1
	else:
		roll = roll2
	if roll >= 5:
		suc_a5 += 1
	if roll >= 10:
		suc_a10 += 1
	if roll >= 15:
		suc_a15 += 1

for i in range(rolls):
	roll1 = random.randint(1, 20)
	roll2 = random.randint(1, 20)
	if roll1 < roll2:
		roll = roll1
	else:
		roll = roll2
	if roll >= 5:
		suc_d5 += 1
	if roll >= 10:
		suc_d10 += 1
	if roll >= 15:
		suc_d15 += 1

avg5 = suc5 / rolls
avg10 = suc10 / rolls
avg15 = suc15 / rolls

avg_a5 = suc_a5 / rolls
avg_a10 = suc_a10 / rolls
avg_a15 = suc_a15 / rolls

avg_d5 = suc_d5 / rolls
avg_d10 = suc_d10 / rolls
avg_d15 = suc_d15 / rolls

print(
	f'|        |  DC 5  |  DC10  |  DC15  |\n|:------:|:------:|:------:|:------:|\n| Normal |{avg5}|{avg10}|{avg15}|\n| Advantage |{avg_a5}|{avg_a10}|{avg_a15}|\n| Disadvantage |{avg_d5}|{avg_d10}|{avg_d15}|')
