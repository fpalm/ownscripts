# Testet, wie viele Primzahlen unter n es gibt

def isPrim(n):
	i = 2
	while i <= n/2:
		if n%i == 0:
			return False
			break
		i += 1
	else:
		return True

count = 0
n = 1000
for i in range(2, n):
	if isPrim(i): count += 1

print count
