n = int(input())
vals = [*map(int, input().split(" "))]
res = [i for i in range(1, n+1)]
idx = 0
while len(res) != 1:
    idx = (idx + vals[res[idx] - 1] - 1 + len(res))%len(res)
    res.pop(idx)
    idx %= len(res)
print(res[0])