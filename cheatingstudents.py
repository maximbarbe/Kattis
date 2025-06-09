from math import inf, dist
import heapq


n = int(input())
heap = []
for i in range(n):
    x, y = map(float, input().split())
    heap.append((inf, x, y))
heap[0] = (0, heap[0][1], heap[0][2])

res = 0
while heap != []:
    curd, curx, cury = heapq.heappop(heap)
    res += curd
    for i in range(len(heap)):
        distance = abs(curx - heap[i][1]) + abs(cury - heap[i][2])
        if distance < heap[i][0]:
            heap[i] = (distance, heap[i][1], heap[i][2])
    
    
    
    heapq.heapify(heap)
    
    
    
print(int(res)*2)