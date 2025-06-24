from collections import defaultdict, deque
import sys

sys.setrecursionlimit(10**6)


def dfs(prev, src, visited, idx, path):
    visited[src] = True
    path[src] = idx
    for dest in edges[src]:
        if not visited[dest]:
            visited[dest] = True
            dfs(src, dest, visited, idx + 1, path)
        else:
            if dest != prev:
                if (idx - path[dest]) % 2 == 0:
                    print("no way")
                    exit()
n, m = map(int, input().split())
edges = defaultdict(lambda:[])
visited = defaultdict(lambda:False)
for i in range(m):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)
    
for i in range(n):
    path = {}
    if not visited[i]:
        dfs(None, i, visited, 0, path)
print("attend here")