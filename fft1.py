import numpy as np
import pylab as pl

bins = np.arange(0, 1, 0.01)

y = pl.normpdf(bins, 0.5, 0.1)
l = pl.plot(bins, y, 'r', linewidth=1)

fourier = np.fft.fft(y)
print fourier

pl.grid(True)
pl.show()
