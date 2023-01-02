rep = int(input())
vote = []
for i in range(rep):
    vote.append(input())

if vote.count('1') > vote.count('0'):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")