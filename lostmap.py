import heapq
from math import inf

# Prim's algorithm
        
nodes = []
visited = []
grid = []
n = int(input())
for i in range(n):
    if i == 0:
        nodes.append((0, (i, None)))

    else:
        nodes.append((inf, (i, None)))
for i in range(n):
    grid.append(list(map(int, input().split(" "))))
heapq.heapify(nodes)

while len(nodes) != 0:
    cur = heapq.heappop(nodes)
    visited.append((cur[1][1], cur[1][0]))
    for i in range(len(nodes)):
        if grid[cur[1][0]][nodes[i][1][0]] < nodes[i][0]:
            nodes[i] = (grid[cur[1][0]][nodes[i][1][0]],  (nodes[i][1][0], cur[1][0]))
    heapq.heapify(nodes)
for x, y in visited:
    if x == None:
        continue
    else:
        print(f"{min(x, y) + 1} {max(x, y) + 1}")