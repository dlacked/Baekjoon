f = [0, 1]
n = int(input())
while 1:
    if len(f)-1 == n:
        break
    f.append(f[-1] + f[-2])
print(f[n])