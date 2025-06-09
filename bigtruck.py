from collections import defaultdict
import heapq
from math import inf
n = int(input())

pickup = [*map(int, input().split())]

edges = [[inf for i in range(n)] for j in range(n)]
heap = [(inf, i, 0) for i in range(n)]
heap[0] = (0, 0, 0)
m = int(input())
for i in range(m):
    v1, v2, d = map(int, input().split())
    v1 -= 1
    v2 -= 1
    edges[v1][v2] = d
    edges[v2][v1] = d
    
while heap != []:
    distance, idx, pickedup = heapq.heappop(heap)
    pickedup += pickup[idx]
    if idx == n - 1:
        if distance == inf:
            print("impossible")
        else:
            print(distance, pickedup)
        exit()
    else:
        for i in range(len(heap)):
            if distance + edges[idx][heap[i][1]] < heap[i][0]:
                heap[i] = (distance + edges[idx][heap[i][1]], heap[i][1], pickedup)
            elif distance + edges[idx][heap[i][1]] == heap[i][0]:
                if pickedup > heap[i][2]:
                    heap[i] = (heap[i][0], heap[i][1], pickedup)
        heapq.heapify(heap)