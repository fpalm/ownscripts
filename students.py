from cPickle import dump

inp = open('students.dat','rb')

students={}

for line in inp:
	ls = linesplit = line.split('\t')
	# print linesplit[1]
	students[ls[1]] = [ls[0], ls[2].strip('\n')]

inp.close()

#print students

out = open('students.pickle', 'wb')
dump(students, out)
out.close()
