# 34scoringmatrix.py by Henry Li and Lisa Yuan

nts = 'ACGT'

print(' ', end = ' ')

for nt in nts:
	if nt == 'T':
		print(' ' + nt)
		break
	print(' ' + nt, end = ' ')

for nt in nts:
	if nt == 'A':
		scores = ' +1 -1 -1 -1'
	if nt == 'C':
		scores = ' -1 +1 -1 -1'
	if nt == 'G':
		scores = ' -1 -1 +1 -1'
	if nt == 'T':
		scores = ' -1 -1 -1 +1'
	print(nt + scores)
