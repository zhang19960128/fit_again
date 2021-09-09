import numpy as np
import os.path
Ha=27.2114
def obtainenergy(filename):
  ETOT=0;
  f=open(filename,'r');
  lines=f.readlines();
  length=len(lines);
  for i in range(length):
    if lines[i].find("ETOT")!=-1:
      ETOT=float(lines[i].split()[2])*Ha;
  f.close();
  return ETOT
def paddingzero(coupling,modelist,position):
  morelist=[0 for i in range(len(modelist))];
  for i in range(len(coupling)):
    morelist[modelist.index(coupling[i])]=position[i];
  return morelist
def outputstring(coupling,modelist,position,Energy):
  plist=paddingzero(coupling,modelist,position);
  outstr="";
  for i in range(len(plist)):
    outstr=outstr+"{0:10.7f}".format(plist[i]);
  outstr=outstr+"{0:15.7f}".format(Energy);
  return outstr
modelist=[2,11,13,15,19,21,22,29];
threemode=open("THREEMODE.dat",'w');
for mode1 in modelist:
  for mode2 in modelist:
    for mode3 in modelist:
      if mode1 < mode2 and mode2 < mode3:
        for i in range(-10,10+2,2):
          for j in range(-10,10+2,2):
            for k in range(-10,10+2,2):
              filename="./MODE{0:d}MODE{1:d}MODE{2:d}/INT{3:d}_{4:d}_{5:d}/MODE{0:d}MODE{1:d}MODE{2:d}INTER{3:d}INTER{4:d}INTER{5:d}.abo".format(mode1,mode2,mode3,i,j,k);
              if os.path.isfile(filename):
                output=outputstring([mode1,mode2,mode3],modelist,[i/10.0,j/10.0,k/10.0],obtainenergy(filename));
                threemode.write(output+"\n");
threemode.close();
