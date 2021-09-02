import numpy as np
import functionscount
from itertools import combinations
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
  print(powerlist)
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
    expandlist.append(blanklist);
  return expandlist;
modelist=[2,11,13,15,19,21,22,29];
for i in modelist:
  for j in modelist:
    for k in modelist:
      for m in modelist:
        for n in modelist:
          if i < j and j < k and k < m and m < n:
            powerlist=generateall([i,j,k,m,n],4);
            print(expand([i,j,k,m,n],modelist,powerlist));
