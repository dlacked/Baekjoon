import sys
sys.stdin.readline()
sg = set(map(int, sys.stdin.readline().split()))
sys.stdin.readline()
M = list(map(int, sys.stdin.readline().split()))
M_set = set(M)
for i in M:
    print(1, end=' ') if i in sg else print(0, end=' ')
