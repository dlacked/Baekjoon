xlist = []
ylist = []
for i in range(0, 3):
    x, y = map(int, input().split())
    xlist.append(x)
    ylist.append(y)
    
for i in range(0, 3):
    if xlist.count(xlist[i]) == 1 :
        x4 = xlist[i]
    if ylist.count(ylist[i]) == 1:
        y4 = ylist[i]
print(x4, y4)