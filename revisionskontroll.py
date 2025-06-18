n = int(input())
seen = dict()
vals = [*map(int, input().split())]
res = []
for v in vals:
    if seen.get(v, False) == False:
        res.append(1)
        seen[v] = True
    else:
        res.append(0)
print(*res)