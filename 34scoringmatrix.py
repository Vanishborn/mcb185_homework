# 34scoringmatrix.py by Henry Li and Lisa Yuan
# edits were inspired by Christi's code from Coderie

nts = 'ACGT'

print(' ', end = ' ')

for nt in nts:
	if nt == 'T':
		print(' ' + nt)
		break
	print(' ' + nt, end = ' ')

for nt1 in nts:
	print(nt1, end = ' ')
	for nt2 in nts:
		if nt1 == nt2:
			print('+1', end = ' ')
		else:
			print('-1', end = ' ')
	print()

