# Berechnet das Skalar- und das Vektorprodukt zweier Vektoren

def skalarprod(a, b):
	result = 0
	for i in range(len(a)):
		result += a[i]*b[i]
	return result

def vektorprod(a, b):
	result = [0,0,0]
	result[0] = a[1]*b[2]-a[2]*b[1]
	result[1] = a[2]*b[0]-a[0]*b[2]
	result[2] = a[0]*b[1]-a[1]*b[0]
	return result

a = [0.3, 1.8, -2.2]
b = [-2.5, 3.8, 0.4]
print "Das Skalarprodukt lautet ", skalarprod(a, b)
print "Das Vektorprodukt lautet ", vektorprod(a, b)
