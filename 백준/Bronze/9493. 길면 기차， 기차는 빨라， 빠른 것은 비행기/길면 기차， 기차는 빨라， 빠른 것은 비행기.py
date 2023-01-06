while 1:
    m, a, b = map(int, input().split())
    if m == 0 and a == 0 and b == 0:
        break
    sec = (m/a - m/b) * 3600
    h = int(sec // 3600)
    mm = round(sec % 3600 // 60)
    ss = round(sec % 3600 % 60)
    
    print(f"{h}:", end="")
    if mm < 10:
        print(f"0{mm}:", end="")
    else:
        print(f"{mm}:", end="")
    if ss < 10:
        print(f"0{ss}")
    else:
        print(f"{ss}")