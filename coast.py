from collections import deque, defaultdict

def bfs(x, y, grid, visited):
    connected_to_edge = False
    cur = 0
    q = deque()
    q.append((x, y))
    visited[(x, y)] = True
    while len(q) != 0:
        x, y = q.popleft()
        if x == 0 or x == n - 1 or y == 0 or y == m - 1:
            connected_to_edge = True
        add = 0
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if x + i < n and x + i >= 0 and y + j < m and y + j >= 0:
                if grid[x + i][y + j] == "1":
                    add += 1
                else:
                    if not visited[(x+i, y+j)]:
                        q.append((x+i, y+j))
                        visited[(x+i, y+j)] = True
        if add != 4:
            cur += add
    if not connected_to_edge:
        return 0
    return cur
n, m = map(int, input().split())
grid = []
for i in range(n):
    grid.append([*input()])

res = 0
visited = defaultdict(lambda:False)
contour = defaultdict(lambda:False)
for i in range(n):
    for j in range(m):
        if grid[i][j] == "0" and not visited[(i, j)]:
            res += bfs(i, j, grid, visited)
if n == 1 and m == 1:
    if grid[0][0] == "1":
        res +=4
    print(res)
    exit()
elif n == 1:
    if grid[0][0] == "1":
        res += 3
    if grid[0][-1] == "1":
        res += 3
    for j in range(1, m-1):
        if grid[0][j] == "1":
            res += 2
    print(res)
    exit()
elif m == 1:
    if grid[0][0] == "1":
        res += 3
    if grid[-1][0] == "1":
        res += 3
    for j in range(1, n-1):
        if grid[j][0] == "1":
            res += 2
    print(res)
    exit()
else:
    if grid[0][0] == "1":
        res += 2
    if grid[0][-1] == "1":
        res += 2
    if grid[-1][0] == "1":
        res += 2
    if grid[-1][-1] == "1":
        res += 2
    for j in range(1, m-1):
        if grid[0][j] == "1":
            res += 1
        if grid[-1][j] == "1":
            res += 1
    for i in range(1, n-1):
        if grid[i][0] == "1":
            res += 1
        if grid[i][-1] == "1":
            res += 1
    print(res)
    exit()