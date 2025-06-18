import heapq
from collections import defaultdict
from math import inf, dist

n, e, p = map(int, input().split())


cables = {}
heap = []
for i in range(n):
    x, y = map(float, input().split())
    cables[i] = set()
    
    heap.append((inf, x, y, i))

for i in range(e):
    heap[i] = (0, heap[i][1], heap[i][2], heap[i][3])

for i in range(p):
    src, dest = map(lambda el: int(el) - 1, input().split())
    cables[src].add(dest)
    cables[dest].add(src)
    
res = 0
heapq.heapify(heap)

while heap != []:
    d, curx, cury, cur = heapq.heappop(heap)
    res += d
    last_idx = None
    for i in range(len(heap)):
        if heap[i][3] in cables[cur]:
            heap[i] = (0, heap[i][1], heap[i][2], heap[i][3])
            
            last_idx = i
        else:
            if dist((curx, cury), (heap[i][1], heap[i][2])) < heap[i][0]:
                heap[i] = (dist((curx, cury), (heap[i][1], heap[i][2])), heap[i][1], heap[i][2], heap[i][3])
                last_idx = i
    heapq.heapify(heap)
        
            
    
print(res)