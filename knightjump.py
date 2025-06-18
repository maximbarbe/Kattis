from collections import deque, defaultdict

moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
n = int(input())

x, y = None, None

grid = []

for i in range(n):
    row = input()
    for j in range(n):
        if row[j] == "K":
            x = i
            y = j
    grid.append(row)

    
    
q = deque()
visited = defaultdict(lambda: False)
q.append((x, y, 0))
visited[(x, y)] = True

while len(q) != 0:
    curx, cury, curmoves = q.popleft()
    
    if curx == 0 and cury == 0:
        print(curmoves)
        exit()
    for x, y in moves:
        if curx + x >= 0 and curx + x < n and cury + y >= 0 and cury + y < n and grid[curx+x][cury+y] != "#" and visited[(curx +x, cury+y)] == False:
            visited[(curx +x, cury+y)] = True
            q.append((curx +x, cury+y, curmoves + 1))
    
    
else:
    print(-1)
