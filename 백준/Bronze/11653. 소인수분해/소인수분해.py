n = int(input())
s = 2
while (n != 1):
    if (n % s == 0):
        print(s)
        n /= s
        s = 2
    else:
        s += 1
