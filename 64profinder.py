# 64profinder.py by Henry Li

import sys
import mcb185
import dogma

def dna_to_protein(seq, min_len):
	protein_list = []

	for i in range(3):
		aaseq = dogma.translate(seq[i:])

		for orf in aaseq.split('*'):
			if 'M' in orf:
				met_index = orf.find('M')
				protein = orf[met_index:]

				if len(protein) >= min_len:
					protein_list.append(protein + '*')

	return protein_list

fasta_path = sys.argv[1]
min_len = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(fasta_path):
	seq_proteins     = dna_to_protein(seq, min_len)
	rev_seq_proteins = dna_to_protein(dogma.revcomp(seq), min_len)
	proteins = seq_proteins + rev_seq_proteins
	for i, protein in enumerate(proteins):
		print(f'>{defline.split()[0]}-prot-{i}\n{protein}')
