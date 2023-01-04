total = 0
n = list(map(int, input().split()))
for i in n:
    total += i*i
print(total % 10)