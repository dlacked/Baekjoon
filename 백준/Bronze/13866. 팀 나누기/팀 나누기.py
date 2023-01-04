t = list(map(int, input().split()))
t.sort()
print(max(t[3] + t[0], t[1] + t[2]) - min(t[3] + t[0], t[1] + t[2]))