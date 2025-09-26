n, p = map(int, input().split())
piles = []
for i in range(p):
    pi, *vals = [*map(int, input().split())]
    piles.append(vals)
m = int(input())
for i in range(m):
    si, di, ni = map(int, input().split())
    t = []
    for j in range(ni):
        t.append(piles[si - 1].pop())
    for j in range(ni):
        piles[di-1].append(t.pop())
for p in piles:
    print(*p)
        