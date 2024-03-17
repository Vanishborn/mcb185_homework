# 74genefinder.py by Henry Li, Jonathan Raigosa, and Conner Suen

import sys
import mcb185

def find_cds(seq, min_orf):
	cds = {}

	for i in range(0, 3):
		while i < len(seq) - min_orf:
			if seq[i:i+3] == 'ATG':
				for j in range(i+3, len(seq)-2, 3):
					if seq[j:j+3] in ['TAA', 'TAG', 'TGA']:
						if j + 2 - i + 1 >= min_orf:
							cds[i+1] = j + 2 + 1
						i = j + 3
						break
			else:
				i += 3

	return cds

min_orf = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defline = defline.split(' ')[0]
	# seq = seq[:10000]

	CDS_forward = find_cds(seq, min_orf)
	CDS_reverse = find_cds(mcb185.anti_seq(seq), min_orf)

	CDS_all = {}
	
	for start, stop in CDS_forward.items():
		CDS_all[start] = stop
	
	for start, stop in CDS_reverse.items():
		CDS_all[len(seq) - stop + 1] = len(seq) - start + 1
	
	for start, stop in sorted(CDS_all.items(), key=lambda item: item[0]):
		if start in CDS_forward:
			print(f'{defline}\tRefSeq\tCDS\t{start}\t{stop}\t.\t+')
		else:
			print(f'{defline}\tRefSeq\tCDS\t{start}\t{stop}\t.\t-')
