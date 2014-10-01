#!/usr/bin/env python

import sys
inputName = sys.argv[1]
outputName = sys.argv[2]

fi=open(inputName)
fo=open(outputName, "w")

for line in fi:
	fo.write(r'\item{'+line+r'}')

fi.close()
fo.close()
