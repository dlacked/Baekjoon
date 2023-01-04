from math import *

a, b, v = map(int, input().split())
day = ceil((v - a) / (a - b) + 1)
print(day)