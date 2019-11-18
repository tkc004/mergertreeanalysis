import numpy as np
import matplotlib.pyplot as plt
import h5py

f = h5py.File('../code/ikea_gals.hdf5', 'r')
dset = f['model0001']
jlevel = np.array(dset['jlevel'][:])
redshift = np.array(dset['redshift'][:])
mhalo = np.array(dset['mhalo'][:]) #in solar mass
mstar = np.array(dset['mstar'][:])*1e12 #in solar mass

zcut = redshift<1e-8
mhaloz0 = mhalo[zcut]
mstarz0 = mstar[zcut]

plt.plot(mhaloz0,mstarz0/mhaloz0,ls='none',marker='o')
plt.xscale('log')
plt.yscale('log')
plt.ylabel('Mstar/Mhalo')
plt.xlabel('Mhalo (Msun)')
plt.title('z = 0')
plt.show()
plt.clf()
