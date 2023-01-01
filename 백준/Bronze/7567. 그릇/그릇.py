string = input()
count = 10
for i in range(1, len(string)):
    if string[i] == '(':
        if (string[i-1] == '('):
            count += 5
        else:
            count += 10
    elif string[i] == ')':
        if (string[i-1] == ')'):
            count += 5
        else:
            count += 10
print(count)