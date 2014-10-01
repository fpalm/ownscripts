lower = 0
upper = 300
step = 20
fahr = lower

while (fahr < upper):
	celsius = 5./9 * (fahr - 32)
	print 'Fahrenheit %6.1f = Celsius %6.3f' %(fahr, celsius)
	#print "Fahrenheit ", fahr, " = Celsius ", celsius
	fahr += step

print "Fertig..."
