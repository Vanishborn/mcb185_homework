# 32fibonacci.py by Henry Li and Lisa Yuan
# edits inspired by Pierce's code from Coderie

# fibi_1 = 1
# fibi_2 = 0

# for i in range(10):
# 	if i == 0:
# 		print(fibi_2)
# 		continue
# 	if i == 1:
# 		print(fibi_1)
# 		continue
# 	fibi = fibi_1 + fibi_2
# 	print(fibi)
# 	fibi_2 = fibi_1
# 	fibi_1 = fibi

def fibonacci(x):
    x1 = -1
    x2 = 1
    for i in range(x):
        total = x1 + x2
        x1 = x2
        x2 = total
        print(total)

fibonacci(9)
