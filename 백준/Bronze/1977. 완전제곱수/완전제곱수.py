from math import *

n1 = int(input())
n2 = int(input())

nlist = []

for i in range(n1, n2+1):
    if sqrt(i) - floor(sqrt(i)) == 0:
        nlist.append(i)
        
if nlist != []:
    print(sum(nlist))
    print(nlist[0])
else:
    print(-1)