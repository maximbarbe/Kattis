from collections import defaultdict
import heapq
from math import inf
grid = []
n,m = map(int, input().split(" "))
for i in range(n):
    grid.append([*map(int, input().split(" "))])
distances = defaultdict(lambda:inf)
visited = defaultdict(lambda: False)
heap = []
for i in range(n):
    for j in range(m):
        heap.append((inf, (i, j)))
heap[0] = (0, (0, 0))
distances[(0, 0)] = 0
while True:
    cur = heapq.heappop(heap)
    visited[cur[1]] = True
    
    i, j = cur[1]
    for x, y in [(0,1), (0, -1), (1, 0), (-1, 0)]:
        if 0 <= x + i < n and 0 <= y + j < m and visited[(x + i, y + j)] == False:
            cost = cur[0] if grid[x + i][y + j] <= grid[i][j] else max(cur[0], grid[x + i][y + j] - grid[i][j])
            if cost < distances[(x + i, y+j)]:
                heapq.heappush(heap, (cost, (x + i, y + j)))
                distances[(x + i, y+j)] = cost
    if visited[(n-1, m-1)]:
        break
print(distances[(n-1, m -1)])