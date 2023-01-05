from math import *

ring = int(input())
time = list(map(int, input().split()))
y, m = 0, 0
for i in range(len(time)):
    y += ((floor(time[i] / 30) + 1) * 10)
    m += ((floor(time[i] / 60) + 1) * 15)
if y == m:
    print(f"Y M {y}")
elif y > m:
    print(f"M {m}")
else:
    print(f"Y {y}")