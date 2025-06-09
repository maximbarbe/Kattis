h1, m1 = map(int, input().split(":"))
h2, m2 = map(int, input().split(":"))
if m2 < m1:
    m2 += 60
    h2 = (h2 - 1)%24
if h2 < h1:
    h2 += 24
res = (h2 - h1)*60 + (m2 - m1)
print(res)