import sys
from collections import Counter
sys.stdin.readline()
sg = Counter(map(int, sys.stdin.readline().split()))
sys.stdin.readline()
M = list(map(int, sys.stdin.readline().split()))
for i in M:
    print(sg[i], end=" ") if i in sg else print(0, end=" ")
