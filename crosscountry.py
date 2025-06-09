from collections import defaultdict
import heapq
from math import inf
n, s, t = map(int, input().split(" "))
grid = []
for i in range(n):
    grid.append([*map(int, input().split(" "))])
distances = defaultdict()
for i in range(n):
    distances[i] = inf
    
distances[s] = 0
heap = []
for key, val in distances.items():
    if val == 0:
        heap.insert(0, (val, key))
    else:
        heap.append((val, key))

while heap != []:
    cur_dist, cur_idx = heapq.heappop(heap)
    if cur_idx == t:
        break
    for i in range(n):
        if grid[cur_idx][i] + cur_dist < distances[i]:
            distances[i] = grid[cur_idx][i] + cur_dist
            for j in range(len(heap)):
                if heap[j][1] == i:
                    heap[j] = (distances[i], i)
                    heapq._siftdown(heap, 0, j)
                    break
    
print(distances[t])