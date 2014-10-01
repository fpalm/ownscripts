import sqlite3

conn = sqlite3.connect('students.sqlite3', isolation_level='DEFERRED')
curs = conn.cursor()

curs.execute('''SELECT * FROM students ORDER BY matrikel''')

result=curs.fetchone()
while result is not None:
	print result
	result = curs.fetchone()

conn.close()
