from collections import deque, defaultdict

n, m =map(int, input().split(" "))

in_queue = defaultdict(lambda:False)
visited = defaultdict(lambda:False)

edges = defaultdict(lambda:[])
for i in range(m):
    x, y = map(int, input().split(" "))
    edges[x].append(y)
    edges[y].append(x)

q = deque()
q.append(1)

while len(q) != 0:
    cur = q.popleft()
    visited[cur] = True
    for dest in edges[cur]:
        if not in_queue[dest] and not visited[dest]:
            q.append(dest)
            in_queue[dest] = True


for i in range(1, n+1):
    if visited[i] == False:
        print("NO")
        exit()
else:
    print("YES")