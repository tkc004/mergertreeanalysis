import numpy as np
import matplotlib.pyplot as plt

ilist = np.linspace(0,10,num=10)
jlist = ilist*10.0
print 'ilist,jlist', ilist,jlist
plt.plot(ilist,jlist,marker='o')
plt.xlim([0,10])
plt.ylim([0,100])
#plt.show()
plt.savefig('test.png')
plt.clf()
