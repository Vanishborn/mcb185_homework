# 23hydropathy.py by Henry Li and Lisa Yuan

import sys

# returns K&D scale value for aa letter
# assuming always valid string input
def kdval(aa):
	aa = aa.upper()
	if   aa ==  "I":
		return 4.5
	elif aa == "V":
		return 4.2
	elif aa == "L":
		return 3.8
	elif aa == "F":
		return 2.8
	elif aa == "C":
		return 2.5
	elif aa == "M":
		return 1.9
	elif aa == "A":
		return 1.8
	elif aa == "G":
		return -0.4
	elif aa == "T":
		return -0.7
	elif aa == "S":
		return -0.8
	elif aa == "W":
		return -0.9
	elif aa == "Y":
		return -1.3
	elif aa == "P":
		return -1.6
	elif aa == "H":
		return -3.2
	elif aa == "Q" or aa == "N" or aa == "E" or aa == "D":
		return -3.5
	elif aa == "K":
		return -3.9
	elif aa == "R":
		return -4.0
	else:
		sys.exit('Error: not on common 20 amino acid alphabet.')

print(kdval("L"))
print(kdval("Q"))
print(kdval("D"))
print(kdval("R"))
print(kdval("B"))
