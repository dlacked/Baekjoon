from sys import *
plug = []
for _ in range(int(stdin.readline())):
    plug.append(int(stdin.readline())-1)
print(sum(plug)+1)