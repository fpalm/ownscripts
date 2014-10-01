from cPickle import load

inp = open('students.pickle', 'rb')
students = load(inp)
inp.close()

check = open('students.dat', 'rb')
for line in check:
	ls = line.split('\t')
	if students[ls[1]] == [ls[0], ls[2].strip('\n')]:
		print "Erfolgreicher Abgleich..."
	else:
		print "Fehler !!!"

check.close()
