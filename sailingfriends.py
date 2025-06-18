def bfs(visited, edges, start_vertex):

    q = deque()
    q.append(start_vertex)
    while len(q) != 0:
        cur = q.popleft()
        visited[cur] = True
        for dest in edges[cur]:
            if visited[dest] == False:
                visited[dest] = True
                q.append(dest)
    return

from collections import defaultdict, deque

n, b, m = map(int, input().split())

friends_with_boat = {i:False for i in range(1, n+1)}
edges = defaultdict(lambda:[])
boats_idx = [*map(int, input().split())]


for i in range(m):
    src, dest = map(int, input().split())
    edges[src].append(dest)
    edges[dest].append(src)
for idx in boats_idx:
    bfs(friends_with_boat, edges, idx)
    
count = 0
for i in range(1, n+1):
    if friends_with_boat[i] == False:
        count += 1
        bfs(friends_with_boat, edges, i)
    
print(count)