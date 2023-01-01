h, m, s = map(int, input().split())
plusSec = int(input())
if (plusSec >= 3600):
    h += plusSec // 3600
    plusSec -= ((plusSec // 3600) * 3600)
if (plusSec >= 60):
    m += plusSec // 60
    plusSec -= ((plusSec // 60) * 60)
    
s += plusSec
if (s >= 60):
    m += s // 60
    s -= ((s//60)*60)
if (m >= 60):
    h += m // 60
    m -= ((m//60)*60)
if (h >= 24):
    h = h % 24
print(h, m, s)