import numpy as np
data=np.loadtxt("POWERTERM.dat");
for i in range(len(data)):
  for j in range(len(data)):
    if i < j:
      dp=np.linalg.norm((data[i]-data[j]));
      if dp < 1e-2:
        print(dp)
