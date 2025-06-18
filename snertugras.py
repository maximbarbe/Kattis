from collections import defaultdict, deque

h, w= map(int, input().split())
grid = []
start = None
for i in range(h):
    row = input()
    for j in range(w):
        if row[j] == "S":
            start = (i, j)
    grid.append(row)
    
visited = defaultdict(lambda: False)
q = deque([(start, 0)])
visited[start] = True
while q:
    pos, count = q.popleft()
    x,y = pos
    for i, j in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        if 0 <= x + i < h and 0 <= y + j < w and visited[(x + i, y+j)] == False:
            if grid[x+i][y+j] == "G":
                print(count + 1)
                exit()
            elif grid[x+i][y + j] == ".":
                visited[(x+i, y+j)] = True
                q.append(((x+i, y+j), count + 1))
else:
    print("thralatlega nettengdur")