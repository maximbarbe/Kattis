from collections import deque, defaultdict


t, n, m = map(int, input().split())
starty, startx = None, None

diff = {
    "U": (1,0),
    "D": (-1, 0),
    "L": (0, 1),
    "R": (0, -1)
}
grid = []
for i in range(n):
    row = input()
    for j in range(m):
        if row[j] == "S":
            starty = i
            startx = j
    grid.append(row)

visited = defaultdict(lambda:False)
q = deque([(starty, startx, 0)])
while len(q) != 0:
    i, j, time = q.popleft()
    visited[(i, j)] = True
    if time > t:
        print("NOT POSSIBLE")
        exit()
    elif i == 0 or i == n - 1 or j == 0 or j == m - 1:
        print(time)
        exit()
    else:
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if i + x >= 0 and i + x < n and j + y  >= 0 and j + y < m and visited[(x+i, y+j)] == False:
                match grid[i + x][y+j]:
                    case "0":
                        q.append((i+x, y+j, time + 1))
                        visited[(i + x, y+j)] = True
                    case "U":
                        if (x, y) == diff["U"]:
                            q.append((i+x, y+j, time + 1))
                            visited[(i + x, y+j)] = True
                    case "D":
                        if (x, y) == diff["D"]:
                            q.append((i+x, y+j, time + 1))
                            visited[(i + x, y+j)] = True
                    case "L":
                        if (x, y) == diff["L"]:
                            q.append((i+x, y+j, time + 1))
                            visited[(i + x, y+j)] = True
                    case "R":
                        if (x, y) == diff["R"]:
                            q.append((i+x, y+j, time + 1))
                            visited[(i + x, y+j)] = True
else:
    print("NOT POSSIBLE")