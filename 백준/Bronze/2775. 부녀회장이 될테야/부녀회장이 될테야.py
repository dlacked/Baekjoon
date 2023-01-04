rep = int(input())
total = 0

for i in range(rep):
    k = int(input())
    n = int(input())
    building_min = list(range(1, n+1))
    for j in range(0, k):
        building = []
        for l in range(0, n):
            building.append(sum(building_min[:l+1]))
        building_min = building
    print(building[-1])