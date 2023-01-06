l = list(map(int, input().split()))
if l == sorted(l):
    print("ascending")
elif l == list(reversed(sorted(l))):
    print("descending")
else:
    print("mixed")