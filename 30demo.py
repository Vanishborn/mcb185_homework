# 30demo.py by Henry Li and Lisa Yuan

import math

# while True:
# 	print('hello')

i = 0
while True:
	i = i + 1
	print('hey', i)
	if i == 3:
		break

i = 0
while i < 3:
	print(i)
	i = i + 1
print('final value of i is', i)

i = 1
while i < 10:
	print(i)
	i = i + 3
print('final value of i is', i)

for i in range(1, 10, 3):
	print(i)

for i in range(0, 5):
	print(i)

for i in range(5):
	print(i)

for char in 'hello':
	print(char)

seq = "GAATTC"
for nt in seq:
	print(nt)

for nt1 in 'ACGT':
	for nt2 in 'ACGT':
		if nt1 == nt2:
			print(nt1, nt2, '+1')
		else:
			print(nt1, nt2, '-1')

nts = 'ACGT'
for nt1 in nts:
	for nt2 in nts:
		if nt1 == nt2:
			print(nt1, nt2, '+1')
		else:
			print(nt1, nt2, '-1')

limit = 4
for i in range(0, limit):
	for j in range(i+1, limit):
		print(i+1, j+1)

# Algorithms

def gc_comp(seq):
	gc_count = 0
	total = 0
	for nt in seq:
		if nt == 'C' or nt == 'G':
			gc_count += 1
		total += 1
	return gc_count / total

print(gc_comp('ACAGCGAAT'))

# Practice

# triangular numbers

def triangular(n):
	tri = 0
	for i in range(n+1):
		tri += i
	return tri

print(triangular(3))

# factorial

def factorial(n):
	if n == 0:
		return 1
	fac = 1
	for i in range(1, n+1):
		fac *= i
	return fac

print(factorial(4))

# euler

def euler(limit):
	e = 0
	for n in range(limit):
		e += 1 / factorial(n)
	return e

print(euler(4))

# is perfect square

def is_perfect_square(n):
	root = math.sqrt(n)
	if math.isclose(root, root // 1):
		return True
	return False

print(is_perfect_square(25))
print(is_perfect_square(10))

# is prime

def is_prime(n):
	for den in range(2, n // 2):
		if n % den == 0:
			return False
		return True

print(is_prime(31415926535897932384626433))
