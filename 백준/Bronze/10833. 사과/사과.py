total = 0
for i in range(int(input())):
    stu, app = map(int, input().split())
    total += app % stu
print(total)