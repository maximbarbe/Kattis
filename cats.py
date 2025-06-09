import heapq
from collections import defaultdict
from math import inf

def update_priority(heap, dest, new_priority):
    for i in range(len(heap)):
        if heap[i][1] == dest:
            heap[i] = (new_priority, heap[i][1])
            break
    heapq._siftdown(heap, 0, i)
    return


# Prim algorithm
# Graph is very dense, so Prim is the choice to find the MST
def prim(edges, visited, distances, M, C):
    tree_cost = C
    heap = [(inf, i) for i in range(C)]
    heap[0] = (0, 0)
    distances[0] = 0
    while heap != []:
        cur = heapq.heappop(heap)
        tree_cost += cur[0]
        idx = cur[1]
        visited[idx] = True
        for edge in edges[idx]:
            if visited[edge[0]] == False and edge[1] < distances[edge[0]]:
                update_priority(heap, edge[0], edge[1])
                distances[edge[0]] = edge[1]


    if tree_cost > M:
        return False
    else:
        return True


n = int(input())
for i in range(n):
    M, C = map(int, input().split(" "))
    visited = dict()
    edges = defaultdict(lambda: [])
    distances = dict()
    for j in range(C):
        visited[j] = False
        distances[j] = inf
    for j in range((C*(C-1))//2):
        src, dest, weight = map(int, input().split(" "))
        edges[src].append((dest, weight))
        edges[dest].append((src, weight))
    if prim(edges, visited, distances, M, C):
        print("yes")
    else:
        print("no")