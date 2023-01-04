ab = list(map(int, input().split()))
cd = list(map(int, input().split()))
print(min(ab[1] + cd[0], ab[0] + cd[1]))