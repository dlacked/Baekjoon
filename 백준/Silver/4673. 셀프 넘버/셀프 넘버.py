set_n = set(range(1, 10001))
del_n = set()

for i in range(1, 10001):
    del_n.add(i + sum(map(int, str(i))))
for i in sorted(set_n - del_n):
    print(i)