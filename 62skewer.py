# 62skewer.py by Henry Li

import sys
import mcb185
import dogma

fapath = sys.argv[1]
window_size = int(sys.argv[2])

all_seq = []

for defline, seq in mcb185.read_fasta(fapath):
	window = seq[:window_size]
	
	for i in range(len(seq) - window_size + 1):
		print(f'{i}\t{dogma.gc_comp(window):.3f}\t{dogma.gc_skew(window):.3f}')
		
		if i != len(seq) - window_size:
			window = window[1:] + seq[i + window_size]
