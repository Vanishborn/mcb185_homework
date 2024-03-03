# 62skewer.py by Henry Li

import sys
import mcb185
import dogma

fapath = sys.argv[1]
window_size = int(sys.argv[2])

# all_seq = []

# for defline, seq in mcb185.read_fasta(fapath):
# 	window = seq[:window_size]
	
# 	for i in range(len(seq) - window_size + 1):
# 		print(f'{i}\t{dogma.gc_comp(window):.3f}\t{dogma.gc_skew(window):.3f}')
		
# 		if i != len(seq) - window_size:
# 			window = window[1:] + seq[i + window_size]

for defline, seq in mcb185.read_fasta(fapath):
	init = seq[:window_size]
	g = init.count('G')
	c = init.count('C')

	print(f'{0}\t{(g + c) / window_size:.3f}\t{(g - c) / (g + c):.3f}')

	for i in range(len(seq) - window_size):
		off = seq[i]
		on = seq[i+window_size]

		if off == 'G':
			g -= 1
		elif off == 'C':
			c -= 1
		if on == 'G':
			g += 1
		elif on == 'C':
			c += 1

		gc_comp = (g + c) / window_size

		if g + c == 0:
			gc_skew = 0
		else:
			gc_skew = (g - c) / (g + c)

		print(f'{i+1}\t{gc_comp:.3f}\t{gc_skew:.3f}')
