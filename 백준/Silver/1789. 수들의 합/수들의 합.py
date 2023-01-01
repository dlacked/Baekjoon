num = int(input())
min = 1
while(True):
    if(num - min < 0):
        break;
    num -= min
    min += 1
print(min-1)