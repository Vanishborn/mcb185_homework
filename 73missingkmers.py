# 73missingkmers.py by Henry Li

import sys
import mcb185
import itertools

def revcomp(seq):
	pairs = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
	rc = ''
	for nt in seq[::-1]:
		rc += pairs[nt]
	return rc

k = 1

while True:
	possible_kmers = {}

	for nts in itertools.product('ACGT', repeat=k):
		possible_kmers[''.join(nts)] = 0

	for defline, seq in mcb185.read_fasta(sys.argv[1]):
		for strand in [seq, revcomp(seq)]:
			for i in range(len(strand) - k + 1):
				kmer = strand[i:i+k]
				possible_kmers[kmer] += 1

	missing_kmers = ()

	for kmer, n in sorted(possible_kmers.items(), key=lambda item: item[1]):
		if n != 0:
			break
		else:
			missing_kmers += (kmer,)

	if len(missing_kmers) != 0:
		print(f'Found {len(missing_kmers)} missing k-mers at k = {k}:')
		for kmer in missing_kmers:
			print(kmer)
		break
	else:
		k += 1
