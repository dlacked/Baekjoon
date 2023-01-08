import sys
sys.stdin.readline()
n1 = set(map(int, sys.stdin.readline().split()))
sys.stdin.readline()
n2 = list(map(int, sys.stdin.readline().split()))
for i in n2:
    if i in n1:
        print(1)
    else:
        print(0)