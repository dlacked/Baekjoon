from sys import *

for _ in range(3):
    total = 0
    for __ in range(int(stdin.readline())):
        total += int(stdin.readline())
    if total > 0:
        print("+")
    elif total < 0:
        print("-")
    else:
        print(0)