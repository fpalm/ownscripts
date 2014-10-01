#!/usr/bin/env python

import pylab
import scipy
import numpy
from numpy import *
from pylab import *
from scipy import *

x = numpy.arange(-100,100,0.01)
y = numpy.zeros_like(x)
# A box of height 1
y [ (x > -0.001) &(x <0.001) ] = 100000.0

clf()
subplot(2, 1, 1)
pylab.plot(x,y)
pylab.axis([-1,1,-0.5,2])

z=numpy.fft.fft(y)
f=numpy.fft.fftfreq(len(y),d=0.01)

subplot(2, 1, 2)
pylab.plot(f,numpy.abs(z))
#pylab.axis([-5,5,0,100])
pylab.show()
