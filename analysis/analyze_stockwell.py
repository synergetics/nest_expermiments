#!/usr/bin/env python

import numpy as np
import pylab
import matplotlib.pyplot as plt

import stockwell.smt as smt
import stockwell


spike_file = 'spikes-103-0.gdf'

voltage_file = 'voltages-104-0.dat'

max_freq = 50
bins = 1000
t_sim = 10000

freq_multiplier = t_sim / bins

spikes = np.genfromtxt(spike_file, delimiter='\t')
time = spikes[:,1]
spike = np.zeros_like(spikes[:,1]) + 1

h = np.histogram(time, bins)

strans = smt.st(h[0], 0, max_freq*freq_multiplier)
strans = abs(strans)

plt.subplot(211)
pylab.plot(h[0], '.')
pylab.title('Binned spike counts')
pylab.ylabel('Spike Count')

plt.subplot(212)
plt.imshow(strans, aspect='auto')
plt.title('Stockwell spectogram')
plt.ylabel('Frequency (Hz*' + str(freq_multiplier) + ')')
plt.xlabel('Time (ms/' + str(freq_multiplier) + ')')

plt.savefig('stockwell.png')
plt.show()

