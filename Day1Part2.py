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
for x in list1:
    for y in list2:
        if(x==y):
            tmp+=1
        #print("-x:",x," -y:",y,"tmp:",tmp)
    results.append(x*tmp)
    tmp=0


    


#print("nummin1:",numMin1,"nummin2:",numMin2)

#for x in results:
    #print("res:",x)
sum=sum(results)
print(sum)
