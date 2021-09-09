import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from mpi4py import MPI
zeroenergy=-9758.5708530;
def function(datapoints,powerlist):
  prod=1.0;
  for i in range(len(powerlist)):
    prod=prod*datapoints[i]**(int(powerlist[i]));
  return prod;
def testfunction(coeff):
  pathcoeff=np.loadtxt("COEFF.dat");
  for j in range(1,8):
    pathcoeff[:,j]=pathcoeff[:,j]/4.0;
  pathcoeff[:,8]=pathcoeff[:,8]/1.0;
  powerlist=np.loadtxt("POWERTERM.dat");
  shape=np.shape(powerlist);
  Plist=pathcoeff[:,0];
  Eall=np.zeros(np.shape(Plist))
  for i in range(len(pathcoeff)):
    for j in range(len(powerlist)):
      Eall[i]=Eall[i]+coeff[j]*function(pathcoeff[i,1:9],powerlist[j]);
  plt.plot(Plist,Eall,'-o');
  plt.xlabel("Polarization(C/m$^2$)")
  plt.ylabel("Energy(eV)")
  plt.show();
  plt.savefig("/workspace/jiahaoz/HZO/LG_Model/GroundP/HfO4/WaveVector/process/FIT/triple/FIT3REp/PYTHONMASTERFIT/newfitting/fitted.png")
  return [Plist,Eall]
modelist=[2,11,13,15,19,21,22,29];
onemode=[];
totaldata=np.loadtxt("./DATAPOINTS/THREE+FOURMODE.dat")
termlist=[];
for i in range(len(modelist)):
  parray=np.loadtxt("./POWER/POWER_{0:d}.dat".format(modelist[i]));
  plist=[list(i) for i in parray]
  termlist=termlist+plist;
for i in range(len(modelist)):
  for j in range(len(modelist)):
    if i < j:
      parray=np.loadtxt("./POWER/POWER_{0:d}_{1:d}.dat".format(modelist[i],modelist[j]))
      plist=[list(i) for i in parray];
      termlist=termlist+plist;
for i in range(len(modelist)):
  for j in range(len(modelist)):
    for k in range(len(modelist)):
      if i < j and j < k:
        parray=np.loadtxt("./POWER/POWER_{0:d}_{1:d}_{2:d}.dat".format(modelist[i],modelist[j],modelist[k]));
        plist=[list(i) for i in parray];
        termlist=termlist+plist;
for i in range(len(modelist)):
  for j in range(len(modelist)):
    for k in range(len(modelist)):
      for m in range(len(modelist)):
        if i < j and j < k and k < m:
          parray=np.loadtxt("./POWER/POWER_{0:d}_{1:d}_{2:d}_{3:d}.dat".format(modelist[i],modelist[j],modelist[k],modelist[m]));
          plist=[list(i) for i in parray];
          termlist=termlist+plist;
fivecouplinglist=[];
for i in range(len(modelist)):
  for j in range(len(modelist)):
    for k in range(len(modelist)):
      for m in range(len(modelist)):
        for n in range(len(modelist)):
          if i < j and j < k and k < m and m < n:
            parray=np.loadtxt("./POWER/POWER_{0:d}_{1:d}_{2:d}_{3:d}_{4:d}.dat".format(modelist[i],modelist[j],modelist[k],modelist[m],modelist[n]));
            plist=[list(i) for i in parray];
            termlist=termlist+plist;
if rank==0:
  termfile=open("POWERTERM.dat",'w');
  for i in range(len(termlist)):
    for j in range(len(modelist)):
      termfile.write("{0:3d}".format(int(termlist[i][j])));
    termfile.write("\n")
  termfile.close();
Xarray=np.zeros((len(totaldata),len(termlist)));
SUMXarray=np.zeros((len(totaldata),len(termlist)));
Yarray=np.zeros(len(totaldata));
SUMYarray=np.zeros(len(totaldata));
comm = MPI.COMM_WORLD;
size=comm.Get_size();
rank=comm.Get_rank();
for i in range(rank,len(totaldata),size):
  for j in range(len(termlist)):
    Xarray[i][j]=function(totaldata[i][0:8],termlist[j]);
  Yarray[i]=totaldata[i][8]-zeroenergy;
  print(i)
comm.Allreduce(Xarray,SUMXarray,op=MPI.SUM);
comm.Allreduce(Yarray,SUMYarray,op=MPI.SUM);
if rank==0:
  print("I am here 0")
  reg=LinearRegression().fit(SUMXarray, SUMYarray);
  [Plist,Eall]=testfunction(reg.coef_);
  f=open("reg_coef",'w');
  for i in range(len(reg.coef_)):
    f.write("{0:d} {1:10.7f}\n".format(i,reg.coef_[i]));
  f.close();
  print("I am here 1 ")
  for i in range(len(Plist)):
    print(Plist[i],Eall[i])
  print("I am here 2 ")
comm.Barrier();
MPI.Finalize();
