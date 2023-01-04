while 1:
    string = input()
    if string == "END":
        break
    string = ''.join(map(str, list(reversed(string))))
    print(string)