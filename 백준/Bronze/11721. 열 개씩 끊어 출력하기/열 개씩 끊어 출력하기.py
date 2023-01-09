import sys
string = sys.stdin.readline()
for i in range(len(string)):
    if i > 0 and (i) % 10 == 0:
        print()
    print(string[i], end="")