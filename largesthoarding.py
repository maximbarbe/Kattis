n = int(input())
buildings = []
for i in range(n):
    h, w = map(int, input().split())
    buildings.append((h, w))
res = 0
for j in range(101):
    cur = 0
    for i in range(n):
        if buildings[i][0] >= j:
            cur += j * buildings[i][1]
        else:
            cur = 0
        res = max(res, cur)
print(res * 50)