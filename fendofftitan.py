import heapq
from collections import defaultdict
from math import inf

# dijkstra algorithm
n, m, src, dest = map(int, input().split(" "))
heap = [(0, 0, 0, src)]
edges = defaultdict(lambda: [])
visited = defaultdict(lambda:False)
distances = defaultdict(lambda: (inf, inf, inf))

for i in range(m):
    s, d, weight, ci = map(int, input().split(" "))
    edges[s].append((d, weight, ci))
    edges[d].append((s, weight, ci))
    
while len(heap) != 0 and visited[dest] == False:
    cur = heapq.heappop(heap)
    visited[cur[3]] = True
    for edge in edges[cur[3]]:
        if visited[edge[0]] == False:
            titan, shaman, length, idx = cur
            if edge[2] == 1:
                shaman += 1
            elif edge[2] == 2:
                titan += 1
            length += edge[1]
            if titan < distances[edge[0]][0]:
                distances[edge[0]] = (titan, shaman, length)
                heapq.heappush(heap, (titan, shaman, length, edge[0]))
            elif titan == distances[edge[0]][0]:
                if shaman < distances[edge[0]][1]:
                    distances[edge[0]] = (titan, shaman, length)
                    heapq.heappush(heap, (titan, shaman, length, edge[0]))  
                elif shaman == distances[edge[0]][1]:
                    if length < distances[edge[0]][2]:
                        distances[edge[0]] = (titan, shaman, length)
                        heapq.heappush(heap, (titan, shaman, length, edge[0]))  
            
            
            
if distances[dest] == (inf, inf, inf):
    print("IMPOSSIBLE")
else:
    print(f"{distances[dest][2]} {distances[dest][1]} {distances[dest][0]}")