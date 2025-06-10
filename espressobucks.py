n, m = map(int, input().split(" "))
grid = []
for i in range(n):
    grid.append([*input()])
for i in range(n):
    for j in range(m):
        if grid[i][j] == "#":
            continue
        if j - 1 >= 0 and grid[i][j - 1] == "E":
            continue
        if j + 1 < m and grid[i][j + 1] == "E":
            continue
        if i - 1 >= 0 and grid[i - 1][j] == "E":
            continue
        if i + 1 < n and grid[i + 1][j] == "E":
            continue
        grid[i][j] = "E"
for row in grid:
    print("".join(row))