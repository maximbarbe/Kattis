from math import dist, inf
import heapq


t = int(input())
for i in range(t):
    n = int(input())
    heap = []
    for j in range(n):
        x, y = map(float, input().split())
        heap.append((inf, x, y))
    heap[0] = (0, heap[0][1], heap[0][2])
    res = 0
    while heap != []:
        curd, curx, cury = heapq.heappop(heap)
        res += curd
        for i in range(len(heap)):
            if dist((curx, cury), (heap[i][1], heap[i][2])) < heap[i][0]:
                heap[i] = (dist((curx, cury), (heap[i][1], heap[i][2])), heap[i][1], heap[i][2])
        heapq.heapify(heap)
    print(res)