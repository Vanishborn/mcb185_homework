# 20demo.py by Henry Li

import sys
import math

print('hello, again') # greeting

"""
This is a 
multi-line
comment
"""

print(1.5e-2)

print(7 // 3)
print(7 % 3)
print((5 + 5) * 2)

print(math.ceil(math.pi))
print(math.sqrt(9))
print(math.factorial(6))
print(math.pow(4,3))

a = 3
b = 4
c = math.sqrt(a**2 + b**2)
print(c)

print(type(a), type(b), type(c), sep=", ")

"""
def pythagoras(a, b):
	return math.sqrt(a**2 + b**2)

print(pythagoras(3, 4))
print(pythagoras(1, 1))
"""

def pythagoras(a, b):
	if a <= 0: 
		sys.exit('error: a must be greater than 0')
	if b <= 0:
		sys.exit('error: b must be greater than 0')
	return math.sqrt(a**2 + b**2)

# print(pythagoras(-1, 1))

# practice
# positive and negative change
def neg_pos_swap(my_num):
	if type(my_num) != int and type(my_num) != float:
		sys.exit('error: your input should be a number')
	if my_num == 0:
		return my_num
	else:
		return my_num * (-1)

print(neg_pos_swap(0.0))
print(neg_pos_swap(math.pi))
# print(neg_pos_swap("0.0"))

# calculate volume of sphere
def vol_sphere(r):
	if type(r) != int and type(r) != float:
		sys.exit('error: your input should be a number')
	if r <= 0:
		sys.exit('error: r must be greater than 0')
	return (4/3) * math.pi * r ** 3

print(vol_sphere(4))

# convert temperature F to C and K
def temp_convert_F_CK(t):
	if type(t) != int and type(t) != float:
		sys.exit('error: your input should be a number')
	c = 5/9 * (t - 32)
	k = c + 273.15
	return c, k

temp_c, temp_k = temp_convert_F_CK(74)
print(temp_c, temp_k, sep=", ")

# convert speed from mph to kph
def speed_convert_mph_to_kph(spd):
	if type(spd) != int and type(spd) != float:
		sys.exit('error: your input should be a number')
	if spd < 0:
		sys.exit('error: r must be greater than or equal to 0')
	return 1.61 * spd

print(speed_convert_mph_to_kph(60))

# I'm gonna skip OD260 because I forgot what I learned about it

# distance between two pts
def distance_two_pts(x1, y1, x2, y2):
	return math.sqrt((x2-x1)**2 + (y2-y1)**2)

# midpoint between two pts
def midpoint(x1, y1, x2, y2):
	mx = (x1 + x2) / 2
	my = (y1 + y2) / 2
	return mx, my

print(midpoint(1, 1, 3, 3))
print(midpoint(3, 3, -3, -3))

# end of practice

a = 0.3
b = 0.1 * 3
print(abs(a - b))
if abs(a - b) < 1e-9:
	print('close enough')

# more practice

# if number is integer
def is_integer(n):
	if type(n) == int:
		return True
	else:
		return False

# if number is odd, assuming always valid inoput
def is_odd(n):
	if n % 2 == 0:
		return False
	else:
		return True

# if number is a valid probability, assuming always >= 0 float input
def is_valid_prob(f):
	if f >= 0 and f <= 1:
		return True
	else:
		return False

print(is_valid_prob(0.76))
print(is_valid_prob(1.5))

# return molecular weight of a DNA letter
# assuming always string input and nucleotide weights
def m_weight_DNA(mychar):
	mychar = mychar.upper()
	if   mychar == "A":
		return 313.23
	elif mychar == "T":
		return 304.21
	elif mychar == "G":
		return 329.23
	elif mychar == "C":
		return 289.20
	else:
		sys.exit('error: user input is not a valid DNA nucleotide')

print(m_weight_DNA("g"))
# print(m_weight_DNA("U"))

# return complement of DNA letter, assuming always string input
def comp_DNA(mychar):
	mychar = mychar.upper()
	if   mychar == "A":
		return "T"
	elif mychar == "T":
		return "A"
	elif mychar == "G":
		return "C"
	elif mychar == "C":
		return "G"
	else:
		sys.exit('error: user input is not a valid DNA nucleotide')

print(comp_DNA("g"))
# print(comp_DNA("U"))
