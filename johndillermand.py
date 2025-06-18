from collections import deque, defaultdict

h, w = map(int, input().split())
grid = [[char for char in input()] for i in range(h)]
visited = defaultdict(lambda:False)
q = deque([(0, 0)])
visited[(0, 0)] = True
while q:
    i, j = q.popleft()
    grid[i][j] = "."
    for x, y in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
        if 0 <= x + i < h and 0 <= j + y < w and grid[x+i][y+j] in "#O" and not visited[(x+i, y+j)]:
            q.append((x+i, y+j))
            visited[(x+i, y+j)] = True
for row in grid:
    print("".join(row))