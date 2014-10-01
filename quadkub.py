# Berechnet die Quadrat und Kubik-Zahlen von 1 bis n
# Berechnet die Summe dieser Zahlen

n = 150
summe2 = summe3 = 0
for i in range(1, n+1):
	print i, ": \t ", i**2, "\t", i**3
	summe2 += i**2
	summe3 += i**3

print "Summe i**2: ", summe2
print "Summe i**3: ", summe3
