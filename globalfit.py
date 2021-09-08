import numpy as np
modelist=[2,11,13,15,19,21,22,29];
onemode=[];
for i in range(len(modelist)):
  parray=np.loadtxt("./POWER/POWER_{0:d}.dat".format(modelist[i]));
  plist=[list(i) for i in parray]
  onemode=onemode+plist;
print(onemode)
