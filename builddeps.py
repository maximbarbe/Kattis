from collections import defaultdict, deque
import sys

sys.setrecursionlimit(1000000)

def dfs(node, path, edges, visited):
    for edge in edges[node]:
        if not visited[edge]:
            dfs(edge, path, edges, visited)
    else:

        path.append(node)
        visited[node] = True

n = int(input())

edges = defaultdict(lambda:[])
res = []
for i in range(n):
    data = input().split()
    dest = data[0]
    for src in data[1:]:
        edges[src].append(dest.rstrip(":"))
        
src = input()
path = []
dfs(src, path, edges, defaultdict(lambda:False))
for i in range(len(path) - 1,-1, -1):
    print(path[i])