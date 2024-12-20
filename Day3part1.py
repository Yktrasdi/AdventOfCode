import re
f=open("input.txt","r")
str1=""
for line in f:
    str1+=str(line)
arrMul=[]
arrMul=(re.findall(r"mul\(\d{1,3}\,\d{1,3}\)",str1))
sum1=0
for x in arrMul:
    nums=re.findall(r"\d+",x)
    print(nums)
    sum1+=int(nums[0])*int(nums[1])
print(sum1)
