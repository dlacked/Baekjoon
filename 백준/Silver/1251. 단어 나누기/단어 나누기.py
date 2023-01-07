string = input()
dic = []
for j in range(1, len(string)-1):
    for k in range(j+1, len(string)):
        johap = []
        johap.append(''.join(reversed(string[:j])))
        johap.append(''.join(reversed(string[j:k])))
        johap.append(''.join(reversed(string[k:])))
        dic.append(''.join(johap))
print(sorted(dic)[0])