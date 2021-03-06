#!/usr/bin/env python

import sqlite3
import sys

if __name__ == "__main__" :

    data = {}
    ##### IMPORTANT 
    # two modes: read = True to write and fill DB
    #            read = False to read from DB
    read = False

    for arg in sys.argv:
        if arg == '-r':
            read = True

    # Read in studenten.txt
    f = open('studenten.txt')
    lines = f.readlines()
    f.close()
    for line in lines:
        temp = line.split(' ')
        data[temp[1].strip()] = [temp[0].strip(), temp[2].strip(), temp[3].strip()]

    # Write data
    conn = sqlite3.connect('studenten.sqlite3', isolation_level='DEFERRED')
    curs = conn.cursor()

    if read == True:
        for key, values in data.iteritems():
            curs.execute('''INSERT INTO studenten VALUES (?, ?, ?, ?, ?)''', (None, key, values[0], values[1], values[2] ))
        
        conn.commit()

    # Read data

    curs.execute('''SELECT * FROM studenten ORDER BY nachname''')
    result = curs.fetchone()

    print 'Sorted by name\n---------------'
    while result is not None:
        print result
        result = curs.fetchone()

    curs.execute('''SELECT * FROM studenten ORDER BY note''')
    result = curs.fetchone()

    print 'Sorted by mark\n---------------'
    while result is not None:
        print result
        result = curs.fetchone()

    curs.close()

