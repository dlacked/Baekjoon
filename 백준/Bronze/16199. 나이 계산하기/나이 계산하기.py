bd = list(map(int, input().split()))
d = list(map(int, input().split()))
y = d[0] - bd[0]
if (bd[1] < d[1] or (bd[1] == d[1] and bd[2] <= d[2])):
    print(y)
else:
    print(y-1)
print(y + 1)
print(y)