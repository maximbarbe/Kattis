from collections import deque, defaultdict


r,c = map(int, input().split())
grid = []
start_pos = None
for i in range(r):
    grid.append([char for char in input()])
    if start_pos == None:
        for j in range(c):
            if grid[i][j] == "A":
                start_pos = (i, j)
                
visited = defaultdict(lambda: False)
q = deque([(start_pos, [start_pos])])
visited[start_pos] = True
while q:
    cur, path = q.popleft()
    i, j = cur
    if grid[i][j] == "P":
        for i, j in path:
            if grid[i][j] not in "AP":
                grid[i][j] = "X"
        break
    else:
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if grid[i + x][j + y] != "#" and visited[(i + x, j+y)] == False:
                q.append(((i + x, j + y), path + [(i + x, j+y)]))
                visited[(i + x, j+y)]= True
else:
    print("call for help")
    exit()
for row in grid:
    print("".join(row))