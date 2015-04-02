
from __future__ import division

import sys
import numpy as np
sys.path.append('/media/ixaxaar/Steam/src/nest/local/lib/python2.7/site-packages/')
import nest
import nest.raster_plot
import nest.voltage_trace
import uuid
import pylab

nest.SetKernelStatus({"resolution": .001})
u = uuid.uuid4()

nest.CopyModel('ac_generator', u, {'amplitude': 1., 'frequency':  20.})
ac = nest.Create(u)


n = ()
for i in xrange(1,10):
  r = np.random.uniform(1000)
  print r
  n += nest.Create("relaxos_van_der_pol", 1, {"epsilon": r/1000, "input_currents_ex": r/1000})

d = nest.Create("spike_detector")

v = nest.Create('voltmeter', 1, {"withgid": True, "withtime": True})

# nest.Connect(ac, n, 'all_to_all', {'weight': .05, 'model': 'static_synapse'})
nest.Connect(n, n, 'all_to_all', {'weight': .1, 'model': 'static_synapse'})
nest.Connect(v, n)

nest.Simulate("1000")

nest.voltage_trace.from_device(v)
pylab.show()

