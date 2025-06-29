import heapq
from collections import defaultdict
from math import inf

n, m = map(int, input().split())
a,b,k,g = map(int, input().split())
a -= 1
b -= 1
intersections = [*map(lambda el:int(el) - 1, input().split())]
costs = dict()
edges = defaultdict(lambda:[])
for i in range(m):
    u, v, c = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append((v, c))
    edges[v].append((u, c))
    costs[(u, v)] = c
    costs[(v, u)] = c
george = defaultdict(lambda:None)
cur = 0
for i in range(1, len(intersections)):
    george[(min(intersections[i - 1], intersections[i]), max(intersections[i - 1], intersections[i]))] = (cur, cur + costs[(intersections[i - 1], intersections[i])])
    cur += costs[(intersections[i - 1], intersections[i])]
distances = defaultdict(lambda:inf)
heap = [(inf, i) for i in range(n)]
distances[a] = k
heap[a] = (k, a)
heapq.heapify(heap)
visited = defaultdict(lambda:False)
while True:
    cost, vtx = heapq.heappop(heap)
    if visited[vtx]:
        continue
    if vtx == b:
        print(cost - k)
        break
    visited[vtx] = True
    for dest, c in edges[vtx]:
        if george[(min(vtx, dest), max(vtx, dest))] != None:
            start, end = george[(min(vtx, dest), max(vtx, dest))]
            if cost < start or cost >= end:
                if cost + c < distances[dest]:
                    distances[dest] = cost + c
                    heapq.heappush(heap, (cost + c, dest))
            else:
                if cost + c + (end - cost) < distances[dest]:
                    distances[dest] = cost + c + (end - cost)
                    heapq.heappush(heap, (cost + c + (end - cost), dest))
        else:
            if cost + c < distances[dest]:
                distances[dest] = cost + c
                heapq.heappush(heap, (cost + c, dest))
