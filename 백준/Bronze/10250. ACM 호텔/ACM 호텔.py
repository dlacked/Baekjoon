for _ in range(int(input())):
    h, w, n = map(int, input().split())
    n -= 1
    if n // h+1 > 9:
        print(f"{n % h+1}{n // h+1}")
    else:
        print(f"{n % h+1}0{n // h+1}")