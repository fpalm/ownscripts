# ReadArgs.py
# Aufruf in shell:
# python ReadArgs.py  99 3.1415 blabla

import sys
n=0
for arg in sys.argv: # Argumente als Liste von strings
    print "arg %d : %s " % ( n, arg )
    n += 1
#
# arg 0 : ReadArgs.py
# arg 1 : 99
# arg 2 : 3.1415
# arg 3 : blabla

