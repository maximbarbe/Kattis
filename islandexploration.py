from collections import defaultdict, deque



def bfs(start):
    q = deque([start])
    visited = defaultdict(lambda:False)
    visited[start] = True
    res = 0
    while q:
        i, j = q.popleft()
        res += 1
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0<= i + x < r and 0 <= j + y < c and grid[i+x][j + y] == '#' and visited[(i +x, j+y)] == False:
                visited[(i + x, j+y)] = True
                q.append((i+x, j + y))
    return res
r, c= map(int, input().split())
grid = []
start = None
for i in range(r):
    row = input()
    for j in range(c):
        if row[j] == "S":
            start = (i, j)
    grid.append(row)

print(bfs(start))