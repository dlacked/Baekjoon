import sys
l = []
for _  in range(5):
    l.append(int(sys.stdin.readline()))
print(sum(l)//5)
l.sort()
print(l[2])