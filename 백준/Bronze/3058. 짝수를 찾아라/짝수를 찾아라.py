for _ in range(int(input())):
    jjaksu = []
    nums = list(map(int, input().split()))
    for i in nums:
        if i % 2 == 0:
            jjaksu.append(i)
    print(sum(jjaksu), min(jjaksu))