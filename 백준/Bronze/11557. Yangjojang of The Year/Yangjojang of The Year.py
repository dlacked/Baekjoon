rep = int(input())
hmd = {}
for i in range(rep):
    school = int(input())
    for i in range(school):
        name, drink = input().split()
        try:
            hmd[name] += int(drink)
        except:
            hmd[name] = int(drink)
    keys = list(hmd.keys())
    values = list(hmd.values())
    print(keys[values.index(max(values))])