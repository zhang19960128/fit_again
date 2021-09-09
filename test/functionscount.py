import numpy as np
def determinerep(index,repdata):
  for i in range(len(repdata)):
    if np.abs(repdata[i,0]-index) < 1e-5:
      return repdata[i,1];
def Dualmodes(repdata):
  f=open("MODESCOUPLE2.dat",'w');
  length=len(repdata);
  for i in range(length):
    for j in range(i,length):
      if i==j:
        continue;
      f.write("{0:5d} {1:5d} {2:5d} {3:5d}\n".format(int(repdata[i][0]),int(repdata[j][0]),int(determinerep(repdata[i][0],repdata)),int(determinerep(repdata[j][0],repdata))));
  f.close();
def Tripmodes(repdata):
  f=open("MODESCOUPLE3.dat",'w');
  length=len(repdata);
  for i in range(length):
    for j in range(i,length):
      for k in range(j,length):
        if i == j or j ==k:
          continue;
        f.write("{0:5d}".format(int(repdata[i][0])));
        f.write("{0:5d}".format(int(repdata[j][0])));
        f.write("{0:5d}".format(int(repdata[k][0])));
        f.write("{0:5d}".format(int(determinerep(repdata[i][0],repdata))));
        f.write("{0:5d}".format(int(determinerep(repdata[j][0],repdata))));
        f.write("{0:5d}".format(int(determinerep(repdata[k][0],repdata))));
        f.write("\n")
  f.close();
def Fourmodes(repdata):
  f=open("MODESCOUPLE4.dat",'w');
  length=len(repdata);
  for i in range(length):
    for j in range(i,length):
      for k in range(j,length):
        for m in range(k,length):
          if i == j or j ==k or k==m:
            continue;
          f.write("{0:5d}".format(int(repdata[i][0])));
          f.write("{0:5d}".format(int(repdata[j][0])));
          f.write("{0:5d}".format(int(repdata[k][0])));
          f.write("{0:5d}".format(int(repdata[m][0])));
          f.write("{0:5d}".format(int(determinerep(repdata[i][0],repdata))));
          f.write("{0:5d}".format(int(determinerep(repdata[j][0],repdata))));
          f.write("{0:5d}".format(int(determinerep(repdata[k][0],repdata))));
          f.write("{0:5d}".format(int(determinerep(repdata[m][0],repdata))));
          f.write("\n")
  f.close();
def partition(listone,colinear):
  shape=np.shape(colinear);
  total=[];
  for i in range(shape[0]):
    inside=1;
    for j in range(shape[1]):
      if colinear[i][j] in listone:
        inside=inside*1;
      else:
        inside=inside*0;
    if inside==1:
      total.append(colinear[i]);
  return total;
def Fivemodes(repdata):
  f=open("MODESCOUPLE5.dat",'w');
  length=len(repdata);
  colinear4=np.loadtxt("COLINEAR4");
  colinear3=np.loadtxt("COLINEAR3");
  tick=0
  for i in range(length):
    for j in range(i,length):
      for k in range(j,length):
        for m in range(k,length):
          for n in range(m,length):
            if i == j or j ==k or k==m or m==n:
              continue;
            trip3=partition([repdata[i][0],repdata[j][0],repdata[k][0],repdata[m][0],repdata[n][0]],colinear3);
            trip4=partition([repdata[i][0],repdata[j][0],repdata[k][0],repdata[m][0],repdata[n][0]],colinear4);
            f.write("{0:3d}".format(tick));
            tick=tick+1;
            f.write("{0:3d}".format(int(repdata[i][0])));
            f.write("{0:3d}".format(int(repdata[j][0])));
            f.write("{0:3d}".format(int(repdata[k][0])));
            f.write("{0:3d}".format(int(repdata[m][0])));
            f.write("{0:3d}".format(int(repdata[n][0])));
            f.write("{0:3d}".format(int(determinerep(repdata[i][0],repdata))));
            f.write("{0:3d}".format(int(determinerep(repdata[j][0],repdata))));
            f.write("{0:3d}".format(int(determinerep(repdata[k][0],repdata))));
            f.write("{0:3d}".format(int(determinerep(repdata[m][0],repdata))));
            f.write("{0:3d}".format(int(determinerep(repdata[n][0],repdata))));
            f.write(" | ");
            for p in range(len(trip3)):
              for q in range(3):
                f.write("{0:3d}".format(int(trip3[p][q])));
              f.write(" | ")
            f.write(" | ")
            for p in range(len(trip4)):
              for q in range(4):
                f.write("{0:3d}".format(int(trip4[p][q])));
              f.write(" | ")
            f.write(" | ")
            f.write("\n")
  f.close();
def progenerate(colinear,modecoupling):
  powerlist=[2 for i in range(len(modecoupling))];
  for i in range(len(colinear)):
    if int(colinear[i]) in modecoupling:
      powerlist[modecoupling.index(colinear[i])]=1;
    else:
      continue;
  return powerlist;
def protofunction(modecoupling):
  colinear4=np.loadtxt("COLINEAR4");
  colinear3=np.loadtxt("COLINEAR3");
  if len(modecoupling)==2:
    powerlist=[];
    if 11 in modecoupling and 29 in modecoupling:
      powerlist.append([1,1]);
    else:
      powerlist.append([2,2]);
    return powerlist;
  if len(modecoupling)==3:
    powerlist=[];
    trip3=partition(modecoupling,colinear3);
    if len(trip3)==0:
      powerlist.append([2 for i in range(len(modecoupling))]);
      return powerlist;
    powerlist.append( progenerate(trip3[0],modecoupling));
    return powerlist;
  if len(modecoupling)==4:
    trip3=partition(modecoupling,colinear3);
    powerlist=[];
    if len(trip3)==0:
      powerlist.append( [2 for i in range(len(modecoupling))] );
    else:
      for i in range(len(trip3)):
        powerlist.append(progenerate(trip3[i],modecoupling));
    trip4=partition(modecoupling,colinear4);
    if len(trip4)==0:
      powerlist.append( [2 for i in range(len(modecoupling))] );
    else:
      for i in range(len(trip4)):
        powerlist.append(progenerate(trip4[i],modecoupling));
    return powerlist;
  if len(modecoupling)==5:
    trip3=partition(modecoupling,colinear3);
    trip4=partition(modecoupling,colinear4);
    powerlist=[];
    for i in range(len(trip3)):
      powerlist.append(progenerate(trip3[i],modecoupling));
    for i in range(len(trip4)):
      powerlist.append(progenerate(trip4[i],modecoupling));
    return powerlist;
def dedup_function(modecoupling):
  powerlist=protofunction(modecoupling);
  additional=[2 for i in range(len(modecoupling))];
  if 11 in modecoupling and 29 in modecoupling:
    additional[modecoupling.index(11)]=1;
    additional[modecoupling.index(29)]=1;
  powerlist.append(additional);
  powerlist.append([2 for i in range(len(modecoupling))]);
  nodup=[];
  [nodup.append(x) for x in powerlist if x not in nodup];
  return nodup;
if __name__=="__main__":
  modelist=[2,11,13,15,19,21,22,29];
  i=2;
  j=11;
  m=13;
  print(i,j,m,dedup_function([i,j,m]))
#  for i in modelist:
#    for j in modelist:
#      for m in modelist:
#        for n in modelist:
#          for t in modelist:
#            if i < j and j < m and m < n and n < t:
#              print(i,j,m,n,t,dedup_function([i,j,m,n,t]))
#  repdata=np.loadtxt("rep.dat");
#  Dualmodes(repdata);
#  Tripmodes(repdata);
#  Fourmodes(repdata);
#  Fivemodes(repdata);
