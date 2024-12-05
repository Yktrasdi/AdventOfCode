f=open("../input.txt","r")
print(f.read())

list1=[3,4,2,1,3,3]
list2=[4,3,5,3,9,3]
results=[]

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
            numMin2=y;
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

for x in results:
    print("res:",x)
