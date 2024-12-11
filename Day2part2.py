f=open("input.txt","r")
numSafe=0
posElim=0
intLineA=[]
for line in f:
    posElim=0
    flag=0
    line=line.replace("\n","")
    lineA=line.split(" ")
    intLineA.clear()
    for x in lineA:
        intLineA.append(int(x))
    
    for i in range(len(intLineA)):
        val=intLineA[i]
        intLineA.pop(posElim)
        
        if(intLineA[0]>intLineA[1]):
            for x in range(len(intLineA)-1):

                if(intLineA[x]-intLineA[x+1]>=1 and intLineA[x]-intLineA[x+1]<=3):
                    flag=1
                else:
                    flag=0
                    break
        elif(intLineA[0]<intLineA[1]):
            for x in range(len(intLineA)-1):
                if(intLineA[x+1]-intLineA[x]>=1 and intLineA[x+1]-intLineA[x]<=3):
                    flag=1
                else:
                    flag=0
                    break
        
        if flag==1:
            numSafe+=1
            break
        else:
            intLineA.insert(posElim,val)
        
        posElim+=1

print(numSafe)
