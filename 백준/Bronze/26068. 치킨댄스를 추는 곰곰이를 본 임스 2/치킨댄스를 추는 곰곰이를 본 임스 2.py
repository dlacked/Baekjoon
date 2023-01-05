count = 0
for _ in range(int(input())):
    dday = input()
    if int(dday[2:]) <= 90:
        count += 1
print(count)