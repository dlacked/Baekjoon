min = -1
for _ in range(int(input())):
    a, b = map(int, input().split())
    if (a <= b and (b <= min or min == -1)):
        min = b
print(min)