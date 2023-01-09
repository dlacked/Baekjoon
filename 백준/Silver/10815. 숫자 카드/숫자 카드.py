import sys
sys.stdin.readline()
sg = set(map(int, sys.stdin.readline().split()))
sys.stdin.readline()
M = list(map(int, sys.stdin.readline().split()))
for i in M:
    print(1, end=' ') if i in sg else print(0, end=' ')
