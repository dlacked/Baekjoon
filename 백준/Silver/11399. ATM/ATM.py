import sys
n = int(sys.stdin.readline())
total = 0
Pi = sorted(list(map(int, sys.stdin.readline().split())))
for i in range(n):
    total += sum(Pi[:i+1])
print(total)