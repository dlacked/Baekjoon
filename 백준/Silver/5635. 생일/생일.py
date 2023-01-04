l = []
for i in range(int(input())):
    n, d, m, y = input().split()
    d, m, y = map(int, (d, m, y))
    l.append([y, m, d, n])
l.sort()
print(l[-1][3])
print(l[0][3])