# 25entropy.py by Henry Li and Lisa Yuan

import math
import sys

# Shannon entropy for nucleotide counts a, c, g, t
# assuming a, c, g, t are all integers
def shannon_entropy(a, c, g, t):
	tot = a + c + g + t

	assert tot != 0, "total nucleotide counts should not be 0"

	aprob = a / tot
	cprob = c / tot
	gprob = g / tot
	tprob = t / tot

	if aprob <= 0:
		sys.exit('error: log2 should only take in values greater than 0')
	aexp = aprob * math.log2(aprob)
	if cprob <= 0:
		sys.exit('error: log2 should only take in values greater than 0')
	cexp = cprob * math.log2(cprob)
	if gprob <= 0:
		sys.exit('error: log2 should only take in values greater than 0')
	gexp = gprob * math.log2(gprob)
	if tprob <= 0:
		sys.exit('error: log2 should only take in values greater than 0')
	texp = tprob * math.log2(tprob)

	entropy = -(aexp + cexp + gexp + texp)

	return entropy

print(shannon_entropy(1, 1, 1, 1))
print(shannon_entropy(100, 500, 500, 100))
print(shannon_entropy(40, 10, 30, 7))
# print(shannon_entropy(0, 0, 0, 0))
