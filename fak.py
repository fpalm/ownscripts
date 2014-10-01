# Berechnet die Fakultaet einer uebergebenen Zahl n

import sys

def fak(n):
	if n == 1:
		return 1
	else:
		return n * fak(n-1)

try:
	print fak(int(sys.argv[1]))
except:
	n = int(input("Bitte gib die Zahl n ein: "))
	print fak(n)
