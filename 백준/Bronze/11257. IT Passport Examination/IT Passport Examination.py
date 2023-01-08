import sys

for _ in range(int(sys.stdin.readline())):
    num, a, b, c = (list(map(int, sys.stdin.readline().split())))
    if a+b+c >= 55 and a >= 35 * (3/10) and b >= 25 * (3/10) and c >= 40 * (3/10):
        print(num, a+b+c, "PASS")
    else:
        print(num, a+b+c, "FAIL")