import numpy as np
import matplotlib.pyplot as plt
import h5py

f = h5py.File('../code/ikea_gals.hdf5', 'r')
dset = f['model0001']
mhalo = dset['mhalo'] #in solar mass
mstar = dset['mstar'] #in 10^12 solar mass
mhalo = np.array(mhalo[:])      #in solar mass
mstar = np.array(mstar[:]*1e12) #in solar mass

plt.plot(mhalo,mstar/mhalo,ls='none',marker='o')
plt.xscale('log')
plt.yscale('log')
plt.ylabel('Mstar/Mhalo')
plt.xlabel('Mhalo (Msun)')
plt.show()
plt.clf()
