import sys
xy = []
for _ in range(int(sys.stdin.readline())):
    xy.append(list(map(int, sys.stdin.readline().split())))
xy.sort(key=lambda x: x[1])
xy.sort()
for i in xy:
    print(i[0], i[1])