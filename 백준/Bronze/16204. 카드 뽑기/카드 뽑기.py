n, m, k = map(int, input().split())
front = [m, n-m]
back = [k, n-k]
print(min(front[0], back[0]) + min(front[1], back[1]))