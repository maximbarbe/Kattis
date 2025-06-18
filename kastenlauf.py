import heapq
from math import inf


def get_minimum(distances, visited):
    cur_min = inf
    idx = None
    for i in range(len(distances)):
        if distances[i] < cur_min and distances[i] <= 1000 and visited[i] == False:
            cur_min = distances[i]
            idx = i
    return idx

t = int(input())
for i in range(t):
    n = int(input())
    visited = [False] * (n+2)
    locations = []
    distances = [0] + [inf] * (n+1)
    distances[0] = 0
    for j in range(n+2):
        locations.append(tuple([*map(int, input().split())]))
        
    while True:
        cur = get_minimum(distances, visited)
    
        if cur == n+1:
            print("happy")
            break
        elif cur == None:
            print("sad")
            break
        visited[cur] = True   
        x, y = locations[cur]   
        for i in range(len(distances)):
            if abs(locations[i][0] - x) + abs(locations[i][1] - y) < distances[i]:
                distances[i] = abs(locations[i][0] - x) + abs(locations[i][1] - y)