# 35nchoosek.py by Henry Li and Lisa Yuan

def factorial(n):
	if n == 0:
		return 1
	fac = 1
	for i in range(1, n+1):
		fac *= i
	return fac

def nchoosek(n, k):
	return factorial(n) / (factorial(k) * factorial(n-k))

print(nchoosek(1, 1))
print(nchoosek(2, 1))
print(nchoosek(3, 2))
print(nchoosek(10, 3))