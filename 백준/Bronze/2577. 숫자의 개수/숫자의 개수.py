l = list(range(0, 10))
n = 1
for _ in range(3):
    n *= int(input())
for i in l:
    print(str(n).count(str(i)))