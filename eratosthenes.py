n = 1000000

zahlliste = range(2, n+1)
gestrichen = []
for i in zahlliste:
	if i not in gestrichen:
		for t in zahlliste[i:]:
			if (t not in gestrichen) and (t%i == 0):
				gestrichen.append(t)

print len(zahlliste)-len(gestrichen)
