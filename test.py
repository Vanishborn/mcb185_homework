# import math

# print(type(print('0')))

# print(type(math.sqrt(4)))

# print(type(math.pow(2,-2)))

# a = 5.6
# b = 5.4
# c = 5.5

# print(int(a//1))
# print(int(b//1))
# print(int(c//1))

# line = 'lol\thellp\thahaha ???'
# line = line.split()
# print(line[0], line[-1])

# mystring = 'lolhellomeow'
# mystring2 = mystring[:5]
# print(mystring2)

# my_tup = ()
# print(len(my_tup))

# seq = "AAATTTCCCG"
# i = 3

# codon = seq[i:i+3]

# print(codon)
# print(seq[i+3])

# if len(codon) == 3:
# 	print("OKAY")

# a = {}
# b = {}

# a[12] = 14
# a[3] = 17
# a[6] = 7
# b[4] = 15
# b[7] = 18
# b[11] = 47

# print(a)
# print(b)

# c = {}

# for k, v in a.items():
#     c[k] = v
    
# for k, v in b.items():
#     c[k] = v

# print(c)

# pos = 'complement(5683..6459)'
# print(pos.strip(')').split('..')[1])

# mystr = '1.1304e+06'
# print(type(type(mystr)))

# if type(mystr) == "<class 'str'>":
#     print('yes')
# else:
#     print('no')


# i = 0

# while i < 6:
# 	print('yes')
# 	i += 1


# def create_pwm(length):
# 	pwm = []
# 	i = 0

# 	while i < length:
# 		pwm.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})
# 		i += 1

# 	return pwm

# testpwm = create_pwm(6)
# print(len(testpwm))

# seq = '1234567890'
# print(seq[-7:])
# print(seq[:-7])

seq = 'ACGTGGTH'


def to_lower(nt):
	nts = 'ACGT'
	nts_lower = 'acgt'

	return nts_lower[nts.index(nt)]

for nt in seq:
	print(to_lower(nt))