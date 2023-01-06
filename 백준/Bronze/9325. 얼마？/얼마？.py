for _ in range(int(input())):
    car = int(input())
    option = int(input())
    for __ in range(option):
        q, p = map(int, input().split())
        car += q*p
    print(car)