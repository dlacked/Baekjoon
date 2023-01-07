string = []
for _ in range(int(input())):
    string.append(input())
string = set(string)
string = list(string)
string.sort()
string.sort(key=lambda x: len(x))
for i in string:
    print(i)