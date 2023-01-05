x, y = map(int, input().split())
a = 100 - x
b = 100 - y
c = 100-(a+b)
if len(str(a*b//100)) >= 2:
    q = int(str(a*b//100)[:2])
else:
    q = a*b//100
if len(str(a*b%100)) >= 2:
    r = int(str(a*b%100)[-2] + str(a*b%100)[-1])
else:
    r = a*b%100
print(a, b, c, a*b, q, r)
print(str(c+q)[:2], r)