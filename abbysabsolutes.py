n, k = map(int, input().split())
vals = [*map(int, input().split())]
res = []
for v in vals:
    if abs(v - 1) <= abs(v - n):
        res.append(1)
    else:
        res.append(n)
        
print(*res)