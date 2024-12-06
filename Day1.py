f=open("input.txt","r")
print(type(f))

list1=[]
list2=[]
results=[]
for x in range(1000):
    tmp=f.readline()
    tmp=str(tmp)
    tmp=tmp.split("   ")
    list1.append(int(tmp[0]))
    list2.append(int(tmp[1]))
    #print("svv",tmp)
    #print("\nasohi",list1[x]," ",list2[x])

tmp=0
for z in range(len(list1)):
    numMin1=max(list1)
    numMin2=max(list2)
    
    for x in list1:
        if(x<numMin1):
            numMin1=x
        #print("x:",x)
    for y in list2:
        if(y<numMin2):
            numMin2=y
        #print("y:",y)
    
    list1.remove(numMin1)
    list2.remove(numMin2)
    #print("min1:",numMin1)
    #print("min2:",numMin2)
    if(numMin1>numMin2):
        tmp=numMin1-numMin2
    elif(numMin1<numMin2):
        tmp=numMin2-numMin1
    else:
        tmp=0
    #print("-x:",x,"\n-y:",y)
    results.append(tmp)


#print("nummin1:",numMin1,"nummin2:",numMin2)

#for x in results:
    #print("res:",x)
sum=sum(results)
print(sum)
