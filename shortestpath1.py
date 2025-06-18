import heapq
from math import inf


first = True
def replace_in_heap(heap, idx, new_dist):
    for i in range(len(heap)):
        if heap[i][1] == idx:
            heap[i] = (new_dist, idx)
            break
    heapq._siftdown(heap, 0, i)

# dijkstra algorithm

while True:

    n, m, q, s = map(int, input().split(" "))
    if n == 0 and m == 0 and q == 0 and s == 0:
        break
    if not first:
        print()
    first = False
    distances = {}
    edges = {}
    heap = []
    for i in range(n):
        distances[i] = inf
        edges[i] = []
        heap.append((inf, i))
    distances[s] = 0
    
    for i in range(m):
        src, dest, weight = map(int, input().split(" ")) 
        edges[src].append((dest, weight))
        
    heap[s] = (0, s)
    heapq.heapify(heap)
    while heap != []:
        cur = heapq.heappop(heap)
        dist = cur[0]
        idx = cur[1]
        for edge in edges[idx]:
            if dist + edge[1] < distances[edge[0]]:
                distances[edge[0]] = dist + edge[1]
                replace_in_heap(heap, edge[0], dist + edge[1])
    for i in range(q):
        idx = int(input())
        print("Impossible" if distances[idx] == inf else distances[idx])