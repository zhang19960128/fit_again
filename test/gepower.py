import numpy as np
import functionscount
from itertools import combinations
POWERFOLDER="./POWER"
def plus2(starttick,finalist):
  secondlist=finalist.copy();
  returntick=len(finalist);
  for i in range(starttick,len(finalist)):
    for j in range(len(finalist[i])):
      worklist=finalist[i].copy();
      worklist[j]=worklist[j]+2;
      secondlist.append(worklist);
  return [returntick,secondlist];
def cutpower(worklist,maxpower):
  sign=1;
  for i in range(len(worklist)):
    if worklist[i] > maxpower:
      sign=sign*0;
    else:
      sign=sign*1;
  return sign
def generatelist(prototype,maxpower):
  [nexttic,nextlist]=plus2(0,prototype)
  [nexttic,nextlist]=plus2(nexttic,nextlist)
  [nexttic,nextlist]=plus2(nexttic,nextlist)
  [nexttic,nextlist]=plus2(nexttic,nextlist)
  filted=list(filter(lambda i:cutpower(i,maxpower),nextlist));
  nodup=[];
  filted.append([2 for i in range(len(prototype[0]))])
  filted.append([4 for i in range(len(prototype[0]))])
  [nodup.append(x) for x in filted if x not in nodup]
  return nodup;
def generateall(modelist,maxpower):
  powerlist=functionscount.dedup_function(modelist);
  outlist=[];
  for i in powerlist:
    outlist=outlist+generatelist([i],maxpower);
  nodup=[];
  [ nodup.append(x) for x in outlist if x not in nodup ];
  return nodup
def expand(modecoupling,modelist,powerlist):
  expandlist=[];
  for i in range(len(powerlist)):
    blanklist=[ 0 for i in range(len(modelist)) ];
    power=powerlist[i];
    for j in range(len(modecoupling)):
      blanklist[modelist.index(modecoupling[j])]=power[j];
    if np.sum(np.array(blanklist)) <= 20:
      expandlist.append(blanklist);
  return expandlist;
def writepower(modecoupling,powerlist):
  filename=POWERFOLDER+"/POWER";
  for i in range(len(modecoupling)):
    filename=filename+"_"+str(modecoupling[i]);
  filename=filename+".dat";
  f=open(filename,'w');
  for i in range(len(powerlist)):
    for j in range(len(powerlist[i])):
      f.write("{0:4d}".format(powerlist[i][j]));
    f.write("\n");
  f.close();
modelist=[2,11,13,15,19,21,22,29];
# Single Mode Coupling
for i in modelist:
  powerlist=[[p] for p in range(2,8+2,2)]
  expandlist=expand([i],modelist,powerlist)
  writepower([i],expandlist)
# Two Mode coupling
for i in modelist:
  for j in modelist:
    if i < j:
      powerlist=generateall([i,j],4);
      expandlist=expand([i,j],modelist,powerlist);
      writepower([i,j],expandlist);
# Third Mode coupling
for i in modelist:
  for j in modelist:
    for k in modelist:
      if i < j and j < k:
        powerlist=generateall([i,j,k],4);
        expandlist=expand([i,j,k],modelist,powerlist);
        writepower([i,j,k],expandlist);
# Four Mode coupling
for i in modelist:
  for j in modelist:
    for k in modelist:
      for m in modelist:
        if i < j and j < k and k < m:
          powerlist=generateall([i,j,k,m],4);
          expandlist=expand([i,j,k,m],modelist,powerlist);
          writepower([i,j,k,m],expandlist);
# Four Mode coupling
for i in modelist:
  for j in modelist:
    for k in modelist:
      for m in modelist:
        for n in modelist:
          if i < j and j < k and k < m and m < n:
            powerlist=generateall([i,j,k,m,n],4);
            expandlist=expand([i,j,k,m,n],modelist,powerlist);
            writepower([i,j,k,m,n],expandlist);
