#!/usr/bin/env python3

import argparse
import math
import mcb185

parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('-s', '--size', type=int, default=20,
					help='window size [%(default)i]')
parser.add_argument('-e', '--entropy', type=float, default=1.4,
					help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action='store_true', help='soft mask')
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy, arg.lower)


def entropy_of_seq(seq):
	nts = 'ACGT'
	entropy = 0

	for nt in nts:
		p = seq.count(nt) / len(seq)
		if p > 0:
			entropy += -p * math.log2(p)

	return entropy


def to_lower(nt):
	nts = ['A', 'C', 'G', 'T']
	nts_lower = ['a', 'c', 'g', 't']

	if nt in nts:
		return nts_lower[nts.index(nt)]
	else:
		return nt


def mask_seq_to_N(seq, w, threshold, soft_mask):
	seq_list = []

	for nt in seq:
		seq_list.append(nt)

	for i in range(len(seq) - w + 1):
		window = seq[i:i+w]
		entropy = entropy_of_seq(window)

		if entropy < threshold:
			for j in range(i, i+w):
				if soft_mask:
					seq_list[j] = to_lower(seq_list[j])
				else:
					seq_list[j] = 'N'

	return ''.join(seq_list)


for defline, seq in mcb185.read_fasta(arg.file):
	seq_masked = mask_seq_to_N(seq, arg.size, arg.entropy, arg.lower)

	print(f'>{defline}')
	for i in range(0, len(seq_masked), 60):
		print(seq_masked[i:i+60])
