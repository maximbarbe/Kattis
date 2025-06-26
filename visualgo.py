import heapq
from collections import defaultdict
from math import inf

edges = defaultdict(lambda:[])
distances = {}
heap = []
visited = []
ways = []
v,e = map(int, input().split())
for i in range(v):
    visited.append(False)
    ways.append(0)
    heap.append((inf, i))
    distances[i] = inf
for i in range(e):
    u, v, w = map(int, input().split())
    edges[u].append((v, w))

s, t = map(int, input().split())
distances[s] = 0
heap[s] = (0, s)
ways[s] += 1
heapq.heapify(heap)


while True:
    cost, vtx = heapq.heappop(heap)
    if vtx == t:
        print(ways[t])
        exit()
    elif visited[vtx]:
        continue
    visited[vtx] = True
    for dest, weight in edges[vtx]:
        if cost + weight < distances[dest]:
            heapq.heappush(heap, (cost + weight, dest))
            distances[dest] = cost + weight
            ways[dest] = ways[vtx]
        elif cost + weight == distances[dest]:
            ways[dest] += ways[vtx]
    
