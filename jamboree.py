n, m = map(int, input().split())
vals = [*map(int, input().split())]
if n <= m:
    print(max(vals))
else:
    vals += [0] * (2*m - n)
    vals.sort()
    res = []
    for i in range(m):
        res.append(vals[i] + vals[-(i + 1)])
    print(max(res))