univ = list(map(int, input().split()))
if sum(univ) >= 100:
    print('OK')
else:
    force = univ.index(min(univ))
    if force == 0:
        print('Soongsil')
    elif force == 1:
        print('Korea')
    else:
        print('Hanyang')