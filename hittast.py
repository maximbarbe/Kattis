from collections import defaultdict
from math import inf
from heapq import *

distances_a = defaultdict(lambda:inf)
distances_b = defaultdict(lambda:inf)
n, m = map(int, input().split())
lodging = [*map(int, input().split())]
edges = defaultdict(lambda:defaultdict(lambda:None))
visited_a = defaultdict(lambda:False)
visited_b = defaultdict(lambda:False)
for i in range(m):
    u,v,a,b = map(int, input().split())
    u -= 1
    v -= 1
    edges[u][v] = (a, b)
    edges[v][u] = (a, b)

distances_a[0] = 0
distances_b[n - 1] = 0

heap_a = [(distances_a[i], i) for i in range(n)]
while heap_a:
    dist, cur = heappop(heap_a)
    if visited_a[cur]:
        continue
    visited_a[cur] = True
    for edge in edges[cur]:
        if not visited_a[edge]:
            if distances_a[edge] > dist + edges[cur][edge][0]:
                distances_a[edge] = dist + edges[cur][edge][0]
                heappush(heap_a, (distances_a[edge], edge))

heap_b = [(distances_b[i], i) for i in range(n)]
heapify(heap_b)
while heap_b:
    dist, cur = heappop(heap_b)
    if visited_b[cur]:
        continue
    visited_b[cur] = True
    for edge in edges[cur]:
        if not visited_b[edge]:
            if distances_b[edge] > dist + edges[cur][edge][1]:
                distances_b[edge] = dist + edges[cur][edge][1]
                heappush(heap_b, (distances_b[edge], edge))
min_cost = inf
for i in range(n):
    min_cost = min(min_cost, distances_a[i] + distances_b[i] + lodging[i])
print(min_cost)