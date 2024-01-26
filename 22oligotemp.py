# 22oligotemp.py by Henry Li and Lisa Yuan

# returns the oligo melting temperature given the number of As, Cs, Gs, and Ts in the oligo
def oligotemp(a, c, g, t):
	totoligo = a + c + g + t
	if totoligo <= 13:
		return (a + t) * 2 + (g + c) * 4
	else:
		return 64.9 + 41 * (g + c - 16.4) / (a + t + g + c)

print(oligotemp(1, 1, 1, 1))
print(oligotemp(4, 4, 4, 4))
print(oligotemp(10, 10, 10, 10))
