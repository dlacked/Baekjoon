i = 0
while 1:
    i += 1
    n = int(input())
    if n == 0:
        break
    names, count = [], [0 for i in range(n)]
    for _ in range(n):
        names.append(input())
    for __ in range(2*n-1):
        num, ab = input().split()
        count[int(num)-1] += 1
    print(i, names[count.index(1)])