# 50demo.py by Henry Li

import gzip
import math

seq = 'GAATTC'
print(seq[0], seq[1])

print(seq[-1])

for nt in seq:
	print(nt, end='')
print()

for i in range(len(seq)):
	print(i, seq[i])

s = 'ABCDEFGHIJ'
print(s[0:5])

print(s[0:8:2])

print(s[0:5], s[:5])
print(s[5:len(s)], s[5:])

print(s, s[::], s[::1], s[::-1])

tax = ('Homo', 'sapiens', 9606)
print(tax)

# s[0] = 'C'
# tax[0] = 'human'

def quadratic(a, b, c):
	x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
	x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
	return x1, x2


x1, x2 = quadratic(5, 6, 1)
print(x1, x2)
intercepts = quadratic(5, 6, 1)
print(intercepts[0], intercepts[1])

nts = 'ACGT'
for i in range(len(nts)):
	print(i, nts[i])

for i, nt in enumerate(nts):
	print(i, nt)

names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
	print(nts[i], names[i])

for nt, name in zip(nts, names):
	print(nt, name)

for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)

nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)

nts.append('C')
print(nts)

last = nts.pop()
print(last)

nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)

nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

nucleotides = nts.copy()
nucleotides.pop()
nucleotides.sort()
print(nts, nucleotides)

items = list()
print(items)
items.append('eggs')
print(items)

stuff = []
stuff.append(3)
print(stuff)

alph = 'ACDEFGHIKLMPQRSVW'
print(alph)
aas = list(alph)
print(aas)

text = 'good day   to you'
words = text.split()
print(words)

line = '1.41,2.72,3.14'
print(line.split(','))

s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)

if 'A' in alph:
	print('yay')
if 'a' in alph:
	print('no')

print('index G?', alph.index('G'))
# print('index Z?', alph.index('Z'))

print('find G?', alph.find('G'))
print('find Z?', alph.find('Z'))

if 'A' in aas:
	idx = aas.index('A')
	print(idx)

# practice

def minimum(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini:
			mini = val
	return mini

def minmax(vals):
	mini = vals[0]
	maxi = vals[0]
	for val in vals:
		if val < mini:
			mini = val
		if val > maxi:
			maxi = val
	return mini, maxi

def mean(vals):
	total = 0
	for val in vals:
		total += val
	return total / len(vals)

def entropy(probs):
	h = 0
	for p in probs:
		h -= p * math.log2(p)
	return h
print(entropy([0.2, 0.3, 0.5]))

def dkl(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += p * math.log2(p/q)
	return d
p1 = [0.4, 0.3, 0.2, 0.1]
p2 = (0.1, 0.3, 0.4, 0.2)
print(dkl(p1, p2))

# with open(path) as fp:
# 	for line in fp:
# 		do_something_with(line)

# fp = open(path)
# for line in fp:
# 	do_something_with(line)
# fp.close()

# with gzip.open(path, 'rt') as fp:
# 	for line in fp:
# 		print(line, end='')

i = int('42')
x = float('0.61803')
