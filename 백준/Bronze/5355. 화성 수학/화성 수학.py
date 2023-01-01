t = int(input())
for i in range(0, t):
    calc = input().split()
    num = float(calc[0])
    for j in calc:
        if j == '@':
            num *= 3
        elif j == '#':
            num -= 7
        elif j == '%':
            num += 5
    print(f"{num:.2f}")