from collections import defaultdict
import heapq
from math import inf
n, k = map(int, input().split())

pos = defaultdict(lambda:[])
distances = defaultdict(lambda:inf)
for i in range(n):
    row = [*map(int, input().split())]
    for j in range(n):
        pos[row[j]].append((i, j))
        
        
heap = []
for i,j in pos[1]:
    distances[(i, j)] = 0
    heap.append((0, 1, i, j))
    
visited = defaultdict(lambda:[])
while heap:
    cost, num, i, j = heapq.heappop(heap)
    if visited[(i, j)]:
        continue
    if num == k:
        print(cost)
        exit()
    visited[(i, j)] = True
    for i2, j2 in pos[num + 1]:
        if cost + abs(i - i2) + abs(j - j2) < distances[(i2, j2)]:
            distances[(i2, j2)] = cost + abs(i - i2) + abs(j - j2)
            heapq.heappush(heap, (cost + abs(i - i2) + abs(j - j2), num + 1, i2, j2))
else:
    print(-1)