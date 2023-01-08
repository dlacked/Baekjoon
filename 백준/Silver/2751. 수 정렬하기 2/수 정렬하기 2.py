import sys
num = []

for _ in range(int(sys.stdin.readline())):
    num.append(int(sys.stdin.readline()))
    
num = sorted(num)
    
for i in num:
    print(i)