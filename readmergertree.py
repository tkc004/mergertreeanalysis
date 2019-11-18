import numpy as np
import h5py

def readmergertree(fname):
    fhdf5 = h5py.File(fname, 'r')
    datalist=[]
    keylist=[]
    for key in fhdf5:
        datalist.append(dict())
        keylist.append(str(key)+"/")
    for i, key in enumerate(keylist):
        fgroup = fhdf5[key]
        for name in fgroup:
            datalist[i][name] = fgroup[name][:]
    fhdf5.close()
    del fhdf5
    return datalist
