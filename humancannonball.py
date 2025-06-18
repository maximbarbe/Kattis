from math import dist, inf
import heapq
from collections import defaultdict

srcX, srcY = map(float, input().split())
endX, endY = map(float, input().split())
points = [(srcX, srcY)]
distances = defaultdict(lambda:inf)
for i in range(int(input())):
    points.append(tuple(map(float, input().split())))
points.append((endX, endY))
heap = []
for i in range(len(points)):
    heap.append((inf, i))
heap[0] = (0, 0)

while heap:
    cost, vtx = heapq.heappop(heap)
    if vtx == len(points) - 1:
        break
    elif vtx == 0:
        for i, (_, vtx2) in enumerate(heap):
            time_needed = dist(points[0], points[vtx2])/5
            if cost + time_needed < distances[vtx2]:
                distances[vtx2] = cost + time_needed
                heap[i] = (cost + time_needed, vtx2)
        heapq.heapify(heap)
    else:
        for i, (_, vtx2) in enumerate(heap):
            walking_distance = dist(points[vtx], points[vtx2])/5
            cannon_distance = 2 + abs(50 - dist(points[vtx], points[vtx2]))/5
            time_needed = min(walking_distance, cannon_distance)
            if cost + time_needed < distances[vtx2]:
                distances[vtx2] = cost + time_needed
                heap[i] = (cost + time_needed, vtx2)
        heapq.heapify(heap)  
print(distances[len(points) - 1])