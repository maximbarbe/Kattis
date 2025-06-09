n = int(input())
edges = [*map(int, input().split(" "))]

edges.sort()
res = 0
for i in range(1, n):
    res += edges[i] + edges[0]
print(res)