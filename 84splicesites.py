# 84splicesites.py by Henry Li

import sys
import gzip
import mcb185


def read_seqs(fasta_file):
	seqs = {}

	for defline, seq in mcb185.read_fasta(fasta_file):
		seqs[defline.split()[0]] = seq

	return seqs


def get_introns(gff_file):
	introns = []

	with gzip.open(gff_file, 'rt') as fp:
		for line in fp:
			line = line.strip().split()

			if line[2] == 'intron' and line[5] != '.':
				chr = line[0]
				start_i = int(line[3]) - 1
				end_i = int(line[4]) - 1
				strand = line[6]
				introns.append((chr, start_i, end_i, strand))

	return introns


def create_pwm(length):
	pwm = []
	i = 0

	while i < length:
		pwm.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})
		i += 1

	return pwm


def fill_pwm(pwm, seq):
	for i in range(len(seq)):
		pwm[i][seq[i]] += 1


def print_pwm(pwm, pwm_ac, pwm_id, pwm_de):
	print('AC', pwm_ac)
	print('XX')
	print('ID', pwm_id)
	print('DE', pwm_de)
	print(f'{"PO":<8}{"A":<8}{"C":<8}{"G":<8}{"T":<8}')

	for i in range(len(pwm)):
		if i+1 < 10:
			print(f'{'0'+str(i+1):<8}'
				  f'{pwm[i]["A"]:<8}'
				  f'{pwm[i]["C"]:<8}'
				  f'{pwm[i]["G"]:<8}'
				  f'{pwm[i]["T"]:<8}')
		else:
			print(f'{i+1:<8}'
				  f'{pwm[i]["A"]:<8}'
				  f'{pwm[i]["C"]:<8}'
				  f'{pwm[i]["G"]:<8}'
				  f'{pwm[i]["T"]:<8}')

	print('XX')
	print('//')


chr_seqs = read_seqs(sys.argv[1])
introns  = get_introns(sys.argv[2])

don_pwm = create_pwm(6)
acc_pwm = create_pwm(7)

for chr, start_i, end_i, strand in introns:
	if strand == "+":
		intron_seq = chr_seqs[chr][start_i:end_i+1]
	else:
		intron_seq = mcb185.anti_seq(chr_seqs[chr][start_i:end_i+1])

	don_seq = intron_seq[:6]
	acc_seq = intron_seq[-7:]

	fill_pwm(don_pwm, don_seq)
	fill_pwm(acc_pwm, acc_seq)

print_pwm(acc_pwm, 'DEMO1', 'ACC', 'splice acceptor')
print_pwm(don_pwm, 'DEMO2', 'DON', 'splice donor')
