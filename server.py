n, m = map(int, input().split(" "))
costs = list(map(int, input().split(" ")))
res = 0
for i in range(len(costs)):
    if m - costs[i] < 0:
        break
    m -= costs[i]
    res += 1
print(res)