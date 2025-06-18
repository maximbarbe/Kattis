from collections import deque, defaultdict
from math import inf
n, m = map(int, input().split())
grid = [input() for i in range(n)]
res = [[inf for i in range(m)] for j in range(n)]
maximum = 0
queues = deque()
for i in range(n):
    for j in range(m):                
        if grid[i][j] == ".":
            res[i][j] = 0

for i in range(n):
    for j in range(m):
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if (grid[i][j] == "T" and ((i + dy < 0 or i + dy == n or j + dx < 0 or j + dx == m) or res[i + dy][j + dx] == 0)):
                res[i][j] = 1
                queues.append((deque([(i, j)]), defaultdict(lambda:False)))
                break

while queues:
    q, visited = queues.popleft()
    while q:
        i, j = q.popleft()
        visited[(i, j)] = True
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= i + dy < n and 0 <= j + dx < m and not visited[(i + dy, j + dx)] and grid[i + dy][j + dx] == "T":
                visited[(i + dy, j + dx)] = True
                if 1 + res[i][j] < res[i + dy][j + dx]:
                    res[i + dy][j + dx] = 1 + res[i][j]
                    q.append((i + dy, j + dx))

for i in range(n):
    for j in range(m):
        maximum = max(maximum, res[i][j])


for i in range(n):
    for j in range(m):
        if res[i][j] == 0:
            res[i][j] = "." * 2 if maximum < 10 else "." * 3
        else:
            if maximum >= 10:
                if res[i][j] >= 10:
                    res[i][j] = "."+str(res[i][j])
                else:
                    res[i][j] = ".." + str(res[i][j])
            else:
                res[i][j] = "." + str(res[i][j])
for line in res:
    print("".join(map(str, line)))