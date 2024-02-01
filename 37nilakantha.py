# 37nilakantha.py by Henry Li and Lisa Yuan

def nilakantha(n):
	pi = 3
	num = 2
	sign = 1

	if n == 1:
		return 3

	for i in range(1, n):
		pi += sign * (4 / (num * (num+1) * (num+2)))
		sign *= -1
		num += 2
	
	return pi

print(nilakantha(1))
print(nilakantha(2))
print(nilakantha(3))
print(nilakantha(10))
print(nilakantha(10000))
print(nilakantha(1000000))