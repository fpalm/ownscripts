import numpy as np
import pylab as pl

data = np.loadtxt('rohr1.dat')

mu = data.mean()
sigma = data.std()

print "mu: \t %5.3f\n sigma:\t %5.3f" %(mu, sigma)

#N,bins = np.histogram(data,54,range=(-70.0,-15.0))
N, bins, patches = pl.hist(data, 54, facecolor='green', alpha=0.75)

# add a 'best fit' line
y = pl.normpdf( bins, mu, sigma)
l = pl.plot(bins, y, 'r--', linewidth=1)

pl.grid(True)

pl.show()
pl.savefig('rohr1.png',dpi=72)
