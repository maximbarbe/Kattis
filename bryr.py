# dijkstra algorithm
from collections import defaultdict
from math import inf
import heapq

n, m = map(int, input().split(" "))
visited = defaultdict()
edges = defaultdict(lambda:[])
distances = {i:inf for i in range(1, n+1)}

distances[1] = 0

heap = []
for i in range(1, n+1):
    visited[i] = False
    heap.append((inf, i))
heap[0] = (0, 1)
    
for i in range(m):
    a, b, c = map(int, input().split(" "))
    edges[a].append((b, c))
    edges[b].append((a, c))
    
while True:
    cur =heapq.heappop(heap)
    if cur[1] == n:
        break
    visited[cur[1]] = True
    for edge in edges[cur[1]]:
        if visited[edge[0]] == False and distances[cur[1]] + edge[1] < distances[edge[0]]:
            distances[edge[0]] = distances[cur[1]] + edge[1]
            heapq.heappush(heap, (distances[cur[1]] + edge[1], edge[0]))
            
print(cur[0])