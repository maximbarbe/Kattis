n = int(input())
vals = [*map(int, input().split(" "))]
sums = set()
cur = sum(vals)
for i in range(len(vals)):
    sums.add(cur - vals[i])
res = list(sums)
res.sort()
print(len(res))
print(" ".join(map(str, res)))