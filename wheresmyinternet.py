from collections import deque, defaultdict

visited = defaultdict(lambda:False)
edges = defaultdict(lambda: [])
added = defaultdict(lambda:False)
n, m = map(int, input().split(" "))
q = deque()
for i in range(m):
    src, dest = map(int, input().split(" "))
    edges[src].append(dest)
    edges[dest].append(src)

q.append(1)
while len(q) != 0:
    cur = q.pop()
    visited[cur] = True
    for dest in edges[cur]:
        if not visited[dest] and not added[dest]:
            q.append(dest)
            added[dest] = True
connected = True
for i in range(1, n+1):
    if visited[i] == False:
        print(i)
        connected = False
if connected:
    print("Connected")