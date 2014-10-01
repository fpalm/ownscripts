import pylab as pl

def collatz( n ):
  count = 0

  while ( n != 1):
    # n gerade ?
    if ( n%2 == 0 ):
      n = n / 2
      
    else:
      n = 3 * n + 1
      
    #print n
    count += 1
  
  return(count)
    
#print n0, count

#n = 27
#print n, collatz(n)

clist = []
nmax = 10000

for n in range(1, nmax+1):
	clist.append(collatz(n))

#ax=pl.subplot(111)
#ax.set_yscale('log')
pl.plot(range(1, nmax+1), clist, 'gx')
pl.grid(True)
pl.show()
