# 65transmembrane_old.py by Henry Li and Lisa Yuan

import sys
import mcb185
import dogma

fasta_path = sys.argv[1]

tm_proteins = []

for defline, seq in mcb185.read_fasta(fasta_path):
	if len(seq) <= 40:
		continue

	name = defline[:60]

	first30 = seq[:30]
	after30 = seq[30:]

	for i in range(len(first30) - 8 + 1):
		if name in tm_proteins:
			break
		potential_sig_seq = first30[i:i+8]
		if dogma.KD_ave(potential_sig_seq) < 2.5 or 'P' in potential_sig_seq:
			continue
		else:
			for j in range(len(after30) - 11 + 1):
				potential_tmreg_seq = after30[j:j+11]
				if dogma.KD_ave(potential_tmreg_seq) < 2.0 or 'P' in potential_tmreg_seq:
					continue
				else:
					tm_proteins.append(name)
					print(name)
					break
