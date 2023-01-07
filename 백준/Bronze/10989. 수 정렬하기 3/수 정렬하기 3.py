from sys import *
nlist = [0] * 10001

for _ in range(int(stdin.readline())):
    nlist[int(stdin.readline())]+=1

for i in range(10001):
    if nlist[i] != 0:
        for j in range(nlist[i]):
            print(i)