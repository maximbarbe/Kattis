from collections import defaultdict


paths = defaultdict(lambda: [])

stuck = int(input())
while True:
    cur = [*map(int, input().split(" "))]
    if cur[0] == -1:
        break
    lower = cur[0]
    for i in range(1, len(cur)):
        paths[cur[i]].append(lower)

cur = stuck
res = []
while paths[cur] != []:
    res.append(cur)
    cur = paths[cur][0]
res.append(cur)
print(" ".join(map(str, res)))