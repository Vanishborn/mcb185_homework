# 21quadratic.py by Henry Li and Lisa Yuan

import math

def quadratic(a, b, c):
	discriminant = b**2 - 4 * a * c
	try:
		x1 = ((-1 * b) + math.sqrt(discriminant)) / (2 * a)
		x2 = ((-1 * b) - math.sqrt(discriminant)) / (2 * a)
	except:
		print("No real roots, assigning them zeros.")
		return 0, 0
	return x1, x2

x1, x2 = quadratic(1, -8, 5)
print(x1, x2, sep=", ")

x1, x2 = quadratic(1, 2, 1)
print(x1, x2, sep=", ")

x1, x2 = quadratic(5, 20, 32)
print(x1, x2, sep=", ")
