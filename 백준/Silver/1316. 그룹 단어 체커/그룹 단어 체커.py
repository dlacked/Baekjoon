import sys
rep = int(input())
for _ in range(rep):
    string = list(input())
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            string[i-1] = '0'
    for i in string:
        if i == '0':
            continue
        elif string.count(i) >= 2:
            rep -= 1
            break
print(rep)