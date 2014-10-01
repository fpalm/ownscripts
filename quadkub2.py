# Demonstriert die Identitaet Summe(i**3) = (Summe(i))**2

summe = summe3 = 0
n=200

for i in range(1, n+1):
	summe3 += i**3
	summe += i
	print i, ": \t ", summe3, "\t = \t", summe**2, "\t ", (summe3 == summe**2)
