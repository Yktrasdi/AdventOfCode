f=open("./Day4/input.txt","r")
tab=[]
aLine=[]
nXmas=0
for line in f:
    aLine=list(line.replace("\n",""))
    tab.append(aLine)
nRow=len(tab)
nCols=len(tab[0])
#orizzontale
for r in range(nRow):
    for c in range(nCols-3):
        if((tab[r][c]=='X' and tab[r][c+1]=='M' and tab[r][c+2]=='A' and tab[r][c+3]=='S') or (tab[r][c]=='S' and tab[r][c+1]=='A' and tab[r][c+2]=='M' and tab[r][c+3]=='X')):
            nXmas+=1
#verticale
for r in range(nRow-3):
    for c in range(nCols):
        if((tab[r][c]=='X' and tab[r+1][c]=='M' and tab[r+2][c]=='A' and tab[r+3][c]=='S') or (tab[r][c]=='S' and tab[r+1][c]=='A' and tab[r+2][c]=='M' and tab[r+3][c]=='X')):
            nXmas+=1
#obliquo destra
for r in range(nRow-3):
    for c in range(nCols-3):
        if((tab[r][c]=='X' and tab[r+1][c+1]=='M' and tab[r+2][c+2]=='A' and tab[r+3][c+3]=='S') or (tab[r][c]=='S' and tab[r+1][c+1]=='A' and tab[r+2][c+2]=='M' and tab[r+3][c+3]=='X')):
            nXmas+=1
#obliquo sinistra
for r in range(nRow-3):
    for c in range(nCols-3):
        if((tab[r][c+3]=='X' and tab[r+1][c+2]=='M' and tab[r+2][c+1]=='A' and tab[r+3][c]=='S') or (tab[r][c+3]=='S' and tab[r+1][c+2]=='A' and tab[r+2][c+1]=='M' and tab[r+3][c]=='X')):
            nXmas+=1
print(nXmas)
