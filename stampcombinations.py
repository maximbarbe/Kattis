n, m = map(int, input().split())
vals = [*map(int, input().split())]
seen = {0:10**6 + 1}
cur = 0
for i in range(len(vals) - 1, -1, -1):
    cur += vals[i]
    seen[cur] = i

for i in range(m):
    q = int(input())
    cur = 0
    if seen.get(q) != None:
        print("Yes")
        continue
    for j, v in enumerate(vals):
        cur += v
        if cur > q:
            print("No")
            break
        if seen.get(q - cur) != None and seen[q-cur] > j:
            print("Yes")
            break
    else:
        print("No")