# dogma.py by Henry Li

def transcribe(dna):
	return dna.replace('T', 'U')


def revcomp(dna):
	rc = []
	for nt in dna[::-1]:
		if nt == 'A':
			rc.append('T')
		elif nt == 'C':
			rc.append('G')
		elif nt == 'G':
			rc.append('C')
		elif nt == 'T':
			rc.append('A')
		else:
			rc.append('N')
	return ''.join(rc)


'''
def translate(dna):
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if   codon == 'ATG': aas.append('M')
		elif codon == 'TAA': aas.append('*')
		else:                aas.append('X')
	return ''.join(aas)
'''


def translate(dna):
	codons = ('TTT', 'TTC', 'TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG',
			  'ATT', 'ATC', 'ATA', 'ATG', 'GTT', 'GTC', 'GTA', 'GTG',
			  'TCT', 'TCC', 'TCA', 'TCG', 'CCT', 'CCC', 'CCA', 'CCG',
			  'ACT', 'ACC', 'ACA', 'ACG', 'GCT', 'GCC', 'GCA', 'GCG',
			  'TAT', 'TAC', 'TAA', 'TAG', 'CAT', 'CAC', 'CAA', 'CAG',
			  'AAT', 'AAC', 'AAA', 'AAG', 'GAT', 'GAC', 'GAA', 'GAG',
			  'TGT', 'TGC', 'TGA', 'TGG', 'CGT', 'CGC', 'CGA', 'CGG',
			  'AGT', 'AGC', 'AGA', 'AGG', 'GGT', 'GGC', 'GGA', 'GGG')
	aminos = 'FFLLLLLLIIIMVVVVSSSSPPPPTTTTAAAAYY**HHQQNNKKDDEECC*WRRRRSSRRGGGG'
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if codon in codons:
			# idx = codons.index(codon)
			# aa = aminos[idx]
			# aas.append(aa)
			aas.append(aminos[codons.index(codon)])
		else:
			aas.append('X')
	return ''.join(aas)


def KD_ave(pseq):
	aminos  = ['I', 'V', 'L', 'F', 'C', 'M', 'A', 'G', 'T', 'S', 'W', 'Y', 'P', 'H', 'E', 'Q', 'D', 'N', 'K', 'R']
	KD_vals = [4.5, 4.2, 3.8, 2.8, 2.5, 1.9, 1.8, -0.4, -0.7, -0.8, -0.9, -1.3, -1.6, -3.2, -3.5, -3.5, -3.5, -3.5, -3.9, -4.5]

	KD_sum = 0
	for aa in pseq:
		KD_sum += KD_vals[aminos.index(aa)]
	
	if len(pseq) <= 0:
		return 0.0
	else:
		return KD_sum / len(pseq)


def gc_comp(seq):
	return (seq.count('C') + seq.count('G')) / len(seq)


def gc_skew(seq):
	c = seq.count('C')
	g = seq.count('G')
	if c + g == 0:
		return 0
	return (g - c) / (g + c)


def tm(seq):
	a = seq.count('A')
	t = seq.count('T')
	g = seq.count('G')
	c = seq.count('C')

	if len(seq) <= 13:
		return (a + t) * 2 + (g + c) * 4
	else:
		return 64.9 + 41 * (g + c - 16.4) / (a + t + g + c)
