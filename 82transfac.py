# 82transfac.py by Henry Li

import sys
import gzip
import json


def read_records(file_path):
	records_in = []

	with gzip.open(file_path, 'rt') as fp:
		record = []

		for line in fp:
			line = line.strip()

			if line == '//':
				records_in.append(record)
				record = []
				continue

			record.append(line)

	return records_in


def format_records(records_in):
	records_out = []
	record = {}

	for item in records_in:
		record["id"] = item[2].split()[1]

		pwms = []
		i = 6

		while True:
			if item[i] == 'XX':
				break

			pwm = {}
			pwm_by_nts = item[i].split()

			j = 1
			for nt in "ACGT":
				pwm[nt] = float(f"{float(pwm_by_nts[j]):.1f}")
				j += 1

			pwms.append(pwm)

			i += 1

		record["pwm"] = pwms

		records_out.append(record)
		record = {}

	return records_out


records_in  = read_records(sys.argv[1])
records_out = format_records(records_in)

print(json.dumps(records_out, indent=4))
