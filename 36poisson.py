# 36poisson.py by Henry Li and Lisa Yuan

import math

def factorial(n):
	if n == 0:
		return 1
	fac = 1
	for i in range(1, n+1):
		fac *= i
	return fac

def poisson(n, k):
	return math.pow(n, k) * math.pow(math.e, (-1) * n) / factorial(k)

print(poisson(5, 10))
print(poisson(4, 5))
print(poisson(10, 10))