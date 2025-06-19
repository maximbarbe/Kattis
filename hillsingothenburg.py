import heapq
from collections import defaultdict
from math import inf

f = lambda el:int(el) - 1

n,m = map(int, input().split())
src, dest = map(f, input().split())


heights = [*map(int, input().split())]
edges = defaultdict(lambda:[])
for i in range(m):
    u, v = map(f, input().split())
    diff_uv = max(heights[u] - heights[v], 0)
    diff_vu = max(heights[v] - heights[u], 0)
    edges[u].append((v, diff_vu))
    edges[v].append((u, diff_uv))


visited = defaultdict(lambda:False)
heap_nodes = dict()
costs = dict()
heap = []
for i in range(n):
    costs[i] = inf
    heap.append([inf, i])
heap[src][0] = 0
heapq.heapify(heap)

while True:
    cost, idx = heapq.heappop(heap)
    if visited[idx]:
        continue
    visited[idx] = True
    if idx == dest:
        print(cost)
        exit()
    for v, edge_cost in edges[idx]:
        if cost + edge_cost < costs[v]:
            costs[v] = cost + edge_cost
            heapq.heappush(heap, [costs[v], v])
    