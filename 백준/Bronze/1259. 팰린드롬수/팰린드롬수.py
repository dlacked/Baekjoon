while (True):
    num = input()
    if num == '0':
        break
    if list(reversed(num)) == list(num):
        print("yes")
    else:
        print("no")
        