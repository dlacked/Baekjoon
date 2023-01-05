stamp = int(input())
cost = int(input())
case = []

if stamp >= 5:
    case.append(cost - 500)
if stamp >= 10:
    case.append(cost * (9/10))
if stamp >= 15:
    case.append(cost - 2000)
if stamp >= 20:
    case.append(cost * (3/4))
if case == []:
    case.append(cost)
    
if min(case) < 0:
    print(0)
else:
    print(int(min(case)))