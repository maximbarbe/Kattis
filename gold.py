from collections import deque, defaultdict


cols, rows = map(int, input().split())
visited = defaultdict(lambda:False)

grid = []
x, y = None, None
for i in range(rows):
    row = []
    line = input()
    for j in range(len(line)):
        row.append(line[j])
        if line[j] == "P":
            x, y = i, j
            
    grid.append(row)
    
q = deque()
q.append((x, y))
visited[(x, y)] = True
res = 0
while len(q) != 0:
    x, y = q.popleft()
    if grid[x][y] == "G":
        res += 1
    for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if grid[x + i][y + j] == "T":
            break
    else:
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if grid[x + i][y + j] in "G." and visited[(x + i, y+j)] == False:
                q.append((x+i, y + j))
                visited[(x+i, y+j)] = True
                
print(res)