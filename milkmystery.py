n, k = map(int, input().split())
vals = [*map(int, input().split())]
res = 0
for i in range(n - k + 1):
    res = max(res, sum(vals[i:i+k]))
print(res)