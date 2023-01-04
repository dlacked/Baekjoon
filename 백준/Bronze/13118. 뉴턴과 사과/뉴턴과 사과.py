people = list(map(int, input().split()))
x, y, r = map(int, input().split())
if x in people:
    print(people.index(x) + 1)
else:
    print(0)