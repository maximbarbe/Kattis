from collections import deque, defaultdict

def bfs(vertex, edges, visited):
    queue = deque()
    queue.append(vertex)
    visited[vertex] = True
    while len(queue) != 0:
        cur = queue.popleft()
        for v in edges[cur]:
            if visited[v] == False:
                queue.append(v)
                visited[v] = True
    return


n = int(input())
for i in range(n):
    num_vertices = int(input())
    visited = defaultdict()
    edges = defaultdict(lambda:[])
    for i in range(num_vertices):
        visited[i] = False
    num_edges = int(input())
    for i in range(num_edges):
        a, b = map(int, input().split(" "))
        edges[a].append(b)
        edges[b].append(a)
    calls = 0
    for i in range(num_vertices):
        if visited[i] == False:
            bfs(i, edges, visited)
            calls += 1
    print(calls - 1)