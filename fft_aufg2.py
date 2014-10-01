#!/usr/bin/env python

import pylab
import numpy
from numpy import *
from pylab import *
from scipy import *

x = arange(-1,1,0.01)
y = zeros_like(x)
y = normpdf(x, 0, 0.25)

clf()
subplot(2, 1, 1)
pylab.plot(x,y)
pylab.axis([-1,1,-0.5,2])

z=numpy.fft.fft(y)
f=numpy.fft.fftfreq(len(y),d=0.01)

subplot(2, 1, 2)
pylab.plot(f,numpy.abs(z))
pylab.axis([-5,5,0,150])
pylab.show()
