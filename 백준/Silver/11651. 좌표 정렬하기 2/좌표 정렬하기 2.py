from sys import *
xy = []
for _ in range(int(stdin.readline())):
    x, y = map(int, stdin.readline().split())
    xy.append([y, x])
xy.sort()
for y, x in xy:
    print(x, y)