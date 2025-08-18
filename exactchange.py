vals=  [150, 30, 15, 5, 1]
res = []
n = int(input())
for v in vals:
    cur = 0
    while n - v >= 0:
        n -= v
        cur += 1
    res.append(cur)
print(*res[::-1])