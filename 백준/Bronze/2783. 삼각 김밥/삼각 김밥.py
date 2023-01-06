def calc():
    global thousand
    w, g = map(float, input().split())
    thousand.append(w*(1000/g))
    
thousand = []
calc()
for _ in range(int(input())):
    calc()
print(f"{min(thousand):.2f}")