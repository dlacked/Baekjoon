while (True):
    count = 0
    string = input()
    if string == '#':
        break
    for i in string.lower():
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            count += 1
    print(count)