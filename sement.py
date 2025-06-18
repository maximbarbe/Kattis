n, k = map(int, input().split())
vals = []
for i in range(n):
    vals.append(int(input()))
seen = dict()
for v in vals:
    if seen.get(v, None) != None:
        print(seen[v], v)
    else:
        seen[k - v] = v
print("Neibb")