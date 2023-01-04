string = input().lower()
count_dic = {}
string_set = set(string)

for i in string_set:
    count_dic[i] = string.count(i)
    
values = list(count_dic.values())
keys = list(count_dic.keys())

if values.count(max(values)) > 1:
    print('?')
else:
    print(keys[values.index(max(values))].upper())