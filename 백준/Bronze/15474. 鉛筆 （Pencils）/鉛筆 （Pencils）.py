import math
n, a, b, c, d = map(int, input().split())
price = [math.ceil(n / a) * b, math.ceil(n / c) * d]
print(min(price))