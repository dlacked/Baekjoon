import sys
acc = []
n, k, l = map(int, sys.stdin.readline().split())
for _ in range(n):
    p1, p2, p3 = map(int, sys.stdin.readline().split())
    if p1 + p2 + p3 >= k and p1 >= l and p2 >= l and p3 >= l:
        acc.append([p1, p2, p3])
print(len(acc))
for i in acc:
    for j in i:
        print(j, end=" ")