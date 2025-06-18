from collections import deque, defaultdict

r, c, = map(int, input().split())
iden, jden = None, None

x,y = None, None
flooded = deque()
visited = defaultdict(lambda:False)
grid = []
for i in range(r):
    row= input()
    temp = []
    for j in range(c):
        if row[j] == "D":
            iden = i
            jden = j
        elif row[j] == "S":
            x, y = i, j
        elif row[j] == "*":
            flooded.append((i, j))
        temp.append(row[j])
    grid.append(temp)

q = deque([(x, y, 0)])
while len(q) != 0:
    next_q = deque()
    next_flood = deque()
    while len(q) != 0:
        i, j, time = q.popleft()
        
        visited[(i, j)] = True
        if grid[i][j] == "D":
            print(time)
            exit()
        elif grid[i][j] != "*":
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if i + x >= 0 and i + x < r and j + y >= 0 and y + j < c and grid[i+x][y+j] in "D." and not visited[(i + x, y + j)]:

                    next_q.append((i+x, y+j, time + 1))
                    visited[(i + x, y +j )] = True
    q = next_q
    while flooded:
        i, j = flooded.popleft()
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if i + x >= 0 and i + x < r and j + y >= 0 and y + j < c and grid[i+x][y+j] in "S.":
                next_flood.append((i+x, y+j))
                grid[i + x][y+j] = "*"
    flooded = next_flood
else:
    print("KAKTUS")