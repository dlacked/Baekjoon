n, m = map(int, input().split())
range1 = []
range2 = []
for i in range(n):
    range1.append(list(map(int, input().split())))
for i in range(n):
    range2.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        print(range1[i][j] + range2[i][j], end = " ")
    print()