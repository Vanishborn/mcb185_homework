# 83kozak.py by Henry Li

import sys
import gzip
import re
import mcb185


def extract_seq(file_path):
	seqs = []
	origin_found = False

	with gzip.open(file_path, 'rt') as fp:
		for line in fp:
			line = line.strip()

			if re.search('ORIGIN', line):
				origin_found = True

			if origin_found:
				if line == '//':
					break
				seqs.append(''.join(line.split()[1:]))

	return ''.join(seqs)


def create_pwm(file_path, seq):
	pwm = []

	for i in range(14):
		pwm.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})

	with gzip.open(file_path, 'rt') as fp:
		for line in fp:
			if line.startswith('     CDS'):
				pos = line.split()[1]

				if re.search('join', line):
					continue

				if re.search('complement', line):
					end_pos = pos.strip(')').split('..')[1]
					kozak = mcb185.anti_seq(seq[int(end_pos)-5:int(end_pos)+9])
				else:
					start_pos = pos.split('..')[0]
					kozak = seq[int(start_pos)-10:int(start_pos)+4]

				for i, nt in enumerate(kozak[:14]):
					if nt == 'a':
						pwm[i]['A'] += 1
					elif nt == 'c':
						pwm[i]['C'] += 1
					elif nt == 'g':
						pwm[i]['G'] += 1
					else:
						pwm[i]['T'] += 1

	return pwm


def print_pwm(pwm):
	print('AC IMTSU001')
	print('XX')
	print('ID ECKOZ')
	print('DE IMTSU001 ECKOZ ; From GenBank')
	print(f'{"PO":<8}{"A":<8}{"C":<8}{"G":<8}{"T":<8}')

	for i in range(14):
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


print_pwm(create_pwm(sys.argv[1], extract_seq(sys.argv[1])))
