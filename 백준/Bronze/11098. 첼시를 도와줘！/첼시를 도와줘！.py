tc = int(input())
for i in range(tc):
    players = {}
    p = int(input())
    for j in range(p):
        c, name = input().split()
        c = int(c)
        players[c] = name
    keys = players.keys()
    values = players.values()
    print(players[max(keys)])