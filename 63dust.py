# 63dust.py by Henry Li

import sys
import mcb185
import math

def entropy_of_seq(seq):
	nts = 'ACGT'
	entropy = 0

	for nt in nts:
		p = seq.count(nt) / len(seq)
		if p > 0:
			entropy += -p * math.log2(p)
	
	return entropy

def mask_seq_to_N(seq, w, threshold):
	seq_list = []

	for nt in seq:
		seq_list.append(nt)

	for i in range(len(seq) - w + 1):
		window = seq[i:i+w]
		entropy = entropy_of_seq(window)

		if entropy < threshold:
			for j in range(i, i+w):
				seq_list[j] = 'N'
	
	return ''.join(seq_list)

fasta_path = sys.argv[1]
w = int(sys.argv[2])
threshold = float(sys.argv[3])

for defline, seq in mcb185.read_fasta(fasta_path):
	seq_masked = mask_seq_to_N(seq, w, threshold)

	print(f'>{defline}')
	for i in range(0, len(seq_masked), 60):
		print(seq_masked[i:i+60])
