import re
f=open("input.txt","r")
str=f.readline()
arrMul=[]
arrMul.append(re.findall(r"mul\(\d{1,3}\,\d{1,3}\)",str))
print(arrMul)