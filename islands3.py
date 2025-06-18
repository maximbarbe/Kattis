from collections import defaultdict, deque

def bfs(start, graph, visited):
    queue = deque()
    queue.append(start)
    while len(queue) != 0:
        cur = queue.popleft()
        visited[cur] = True
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            voisin = (cur[0] + x, cur[1] + y)
            if graph[voisin[0]][voisin[1]] in ["L", "C"] and visited[voisin] == False:
                queue.append(voisin)
                visited[voisin] = True
    return


n, m = map(int, input().split(" "))
grid = []
grid.append("w" * (m + 2))
res = 0
dict = defaultdict(lambda:False)
for i in range(n):
    grid.append("w" + input() + "w")
grid.append("w" * (m + 2))
for i in range(1, n + 1):
    for j in range(1, m+1):
        if grid[i][j] == "L" and dict[(i, j)] == False:
            bfs((i, j), grid, dict)
            res += 1
print(res)