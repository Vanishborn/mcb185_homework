# 65transmembrane.py by Henry Li and Lisa Yuan

import sys
import mcb185
import dogma

def is_valid_region(seq, w, threshold):
	for i in range(len(seq) - w + 1):
			region = seq[i:i+w]
			if dogma.KD_ave(region) >= threshold and 'P' not in region:
				return True
	return False

def find_tm_proteins(seqs):
	tm_proteins = []

	for defline, seq in seqs:
		if len(seq) <= 40 or defline in tm_proteins:
			continue

		first30 = seq[:30]
		after30 = seq[30:]

		if is_valid_region(first30, 8, 2.5):
			if is_valid_region(after30, 11, 2.0):
				tm_proteins.append(defline)
			else:
				continue

	return tm_proteins

seqs = mcb185.read_fasta(sys.argv[1])

tm_proteins = find_tm_proteins(seqs)

for defline in tm_proteins:
	print(defline[:60])
