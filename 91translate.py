#!/usr/bin/env python3

import argparse
import mcb185
import dogma

parser = argparse.ArgumentParser(description='mRNA translator.')
parser.add_argument('file', type=str, help='fasta file of mRNAs')
parser.add_argument('-m', '--min', type=int, default=100, help='minimum protein length[%(default)i]')
parser.add_argument('-a', '--anti', action='store_true', help='also examine the anti-parallel strand')
arg = parser.parse_args()


def dna_to_mrna(seq):
	proteins = []

	proteins.append(dogma.translate(seq))

	if arg.anti:
		rev_seq = mcb185.anti_seq(seq)
		proteins.append(dogma.translate(rev_seq))

	return proteins


for defline, seq in mcb185.read_fasta(arg.file):
	proteins = dna_to_mrna(seq)

	for protein in proteins:
		if len(protein) >= arg.min:
			print(f">{defline}")
			for i in range(0, len(protein), 60):
				print(protein[i:i+60])
