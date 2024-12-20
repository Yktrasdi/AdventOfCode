import re
f=open("input.txt","r")
str1=""
for line in f:
    str1+=str(line)
arrMul=[]
arrMul=(re.findall(r"mul\(\d{1,3}\,\d{1,3}\)|do\(\)|don't\(\)",str1))
sum1=0
do=True
for x in arrMul:
    if(x=="don't()"):
        do=False
    elif(x=="do()"):
        do=True
    else:
        if(do):
            nums=re.findall(r"\d+",x)
            sum1+=int(nums[0])*int(nums[1])
print(sum1)