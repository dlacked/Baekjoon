ch = sa = 100
rep = int(input())
for i in range(rep):
    d_ch, d_sa = map(int, input().split())
    if d_ch > d_sa:
        sa -= d_ch
    elif d_ch < d_sa:
        ch -= d_sa
print(ch)
print(sa)