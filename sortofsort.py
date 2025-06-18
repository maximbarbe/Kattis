n = int(input())
res = [-10**6]
vals = [*map(int, input().split())]
for v in vals:
    if v >= res[-1]:
        res.append(v)
print(*res[1:])