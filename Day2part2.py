import numpy as np
f=open("input.txt","r")
numSafe=0
posElim=0
for line in f:
    flag=0
    lineA=line.split(" ")
    npLineA=np.array(lineA,int)
    for z in lineA:
        lineA.remove(z)
        print ("z:",z)
        if(npLineA[0]>npLineA[1]):
            for x in range(len(npLineA)-1):
                print("x: ",npLineA[x],"x+1: ",npLineA[x+1],"diff: ",(npLineA[x]-npLineA[x+1]),"pos: ",x)

                if(npLineA[x]-npLineA[x+1]>=1 and npLineA[x]-npLineA[x+1]<=3):
                    flag=1
                else:
                    flag=0
                    break
        elif(npLineA[0]<npLineA[1]):
            for x in range(len(npLineA)-1):
                print("x+1: ",npLineA[x+1],"x: ",npLineA[x],"diff: ",(npLineA[x+1]-npLineA[x]),"pos: ",x)
                if(npLineA[x+1]-npLineA[x]>=1 and npLineA[x+1]-npLineA[x]<=3):
                    flag=1
                else:
                    flag=0
                    break
        
        if flag==1:
            numSafe+=1
            break
        npLineA[posElim]=z
        posElim+=1
print(numSafe)