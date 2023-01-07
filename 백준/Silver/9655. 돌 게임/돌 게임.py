stone = int(input())
turn = 0
if stone >= 3:
    turn += stone // 3
    stone %= 3
turn += stone
if turn % 2 == 0:
    print("CY")
else:
    print("SK")