import numpy as np
f=open("input.txt","r")
numSafe=0
for line in f:
    flag=0
    lineA=line.split(" ")
    lineA=np.array(lineA,int)
    if(lineA[0]>lineA[1]):
        for x in range(len(lineA)-1):
            if(lineA[x]-lineA[x+1]>=1 and lineA[x]-lineA[x+1]<=3):
                #print("x: ",lineA[x],"x+1: ",lineA[x+1],"diff: ",(lineA[x]-lineA[x+1]),"pos: ",x)
                flag=1
            else:
                flag=0
                break
    elif(lineA[0]<lineA[1]):
        for x in range(len(lineA)-1):
            if(lineA[x+1]-lineA[x]>=1 and lineA[x+1]-lineA[x]<=3):
                #print("x+1: ",lineA[x+1],"x: ",lineA[x],"diff: ",(lineA[x+1]-lineA[x]),"pos: ",x)
                flag=1
            else:
                flag=0
                break
        
    if flag==1:
        numSafe+=1
print(numSafe)