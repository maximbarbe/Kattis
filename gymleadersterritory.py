from collections import deque


def bfs(src, alliances, edges, visited):
    
    q = deque()
    q.append(src)
    visited[src] = True
    while len(q) != 0:
        cur = q.popleft()
        for dest in edges[cur]:
            alliances[dest] -= 1
            if visited[dest] == False and alliances[dest] <= 1:
                q.append(dest)
                visited[dest] = True



n, k, m = map(int, input().split())

alliances = dict()
edges = dict()
visited = [False for i in range(n)]
k -= 1
for i in range(n):
    alliances[i] = 0
    edges[i] = []
    
for i in range(m):
    v1, v2 = map(lambda el: int(el) - 1, input().split())
    edges[v1].append(v2)
    edges[v2].append(v1)
    alliances[v1] += 1
    alliances[v2] += 1
    
for i in range(n):
    if alliances[i] <= 1:
        bfs(i, alliances, edges, visited)
if visited[k]:
    print("YES")
else:
    print("NO")