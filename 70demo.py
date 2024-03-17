# 70demo.py by Henry Li

import itertools

d = {}
d = dict()

d = {'dog': 'woof', 'cat': 'meow'}
print(d)

print(d['cat'])

d['pig'] = 'oink'
print(d)

d['cat'] = 'mew'
print(d)

del d['cat']
print(d)

# print(d['rat'])

if 'dog' in d:
	print(d['dog'])

for key in d:
	print(f'{key} says {d[key]}')

for k, v in d.items():
	print(k, 'says', v)

# for thing in d.items():
# 	print(thing[0], thing[1])
	
print(d.keys(), d.values(), list(d.values()))

kdtable = {
	'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5, 'M': 1.9, 'A': 1.8,
	'G': -0.4, 'T': -0.7, 'S': -0.8, 'W': -0.9, 'Y': -1.3, 'P': -1.6, 'H': -3.2,
	'E': -3.5, 'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
}

def kd_dict(seq):
	kd = 0
	for aa in seq:
		kd += kdtable[aa]
	return kd/len(seq)


gcode = {
	'AAA': 'K',	'AAC': 'N',	'AAG': 'K',	'AAT': 'N',
	'ACA': 'T',	'ACC': 'T',	'ACG': 'T',	'ACT': 'T',
	'AGA': 'R',	'AGC': 'S',	'AGG': 'R',	'AGT': 'S',
	'ATA': 'I',	'ATC': 'I',	'ATG': 'M',	'ATT': 'I',
	'CAA': 'Q',	'CAC': 'H',	'CAG': 'Q',	'CAT': 'H',
	'CCA': 'P',	'CCC': 'P',	'CCG': 'P',	'CCT': 'P',
	'CGA': 'R',	'CGC': 'R',	'CGG': 'R',	'CGT': 'R',
	'CTA': 'L',	'CTC': 'L',	'CTG': 'L',	'CTT': 'L',
	'GAA': 'E',	'GAC': 'D',	'GAG': 'E',	'GAT': 'D',
	'GCA': 'A',	'GCC': 'A',	'GCG': 'A',	'GCT': 'A',
	'GGA': 'G',	'GGC': 'G',	'GGG': 'G',	'GGT': 'G',
	'GTA': 'V',	'GTC': 'V',	'GTG': 'V',	'GTT': 'V',
	'TAA': '*',	'TAC': 'Y',	'TAG': '*',	'TAT': 'Y',
	'TCA': 'S',	'TCC': 'S',	'TCG': 'S',	'TCT': 'S',
	'TGA': '*',	'TGC': 'C',	'TGG': 'W',	'TGT': 'C',
	'TTA': 'L',	'TTC': 'F',	'TTG': 'L',	'TTT': 'F',
}


def translate(seq):
	pro = []
	for i in range(0, len(seq), 3):
		codon = seq[i:i+3]
		if codon in gcode:
			aa = gcode[codon]
		else:
			aa = 'X'
		pro.append(aa)
	return ''.join(pro)


kdh = {
	'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5,
	'M':  1.9, 'A':  1.8, 'G': -0.4, 'T': -0.7, 'S': -0.8,
	'W': -0.9, 'Y': -1.3, 'P': -1.6, 'H': -3.2, 'E': -3.5,
	'Q': -3.5, 'D': -3.5, 'K': -3.9, 'N': -3.5, 'R': -4.5,
}


def hydropathy(seq):
	s = 0
	for aa in seq:
		s += kdh[aa]
	return s / len(seq)


# count = {}
# for nt in seq:
# 	if nt not in count:
# 		count[nt] = 0
# 	count[nt] += 1

for nts in itertools.product('ACGT', repeat=2):
	print(nts)
