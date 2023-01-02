def mw(button):
    global sec
    if sec // button > 0:
        r_sec = sec
        sec = sec - button*(sec // button)
        return r_sec // button
    else:
        return 0
    
sec = int(input())
o_sec = sec
a = b = c = 0
a += mw(300)
b += mw(60)
c += mw(10)

if (a * 300 + b * 60 + c * 10 == o_sec):
    print(a, b, c)
else:
    print(-1)