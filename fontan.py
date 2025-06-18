from collections import deque



def dfs(grid, i, j):
    grid[i][j] = "V"
    if i + 1 < len(grid):
        if grid[i + 1][j] == "V":
            return
        elif grid[i + 1][j] == ".":
            dfs(grid, i + 1, j)
        elif grid[i + 1][j] == "#":
            if j - 1>=0 and grid[i][j - 1] == ".":
                dfs(grid, i, j - 1)
            if j + 1 < len(grid[i]) and grid[i][j + 1] == ".":
                dfs(grid,i,j+1)
    return
start_pos = []


n, m = map(int, input().split(" "))
grid = []
for i in range(n):
    string = input()
    row = []
    for j in range(m):
        if string[j] == "V":
            start_pos.append((i, j))
        row.append(string[j])
    grid.append(row)
for i, j in start_pos:
    dfs(grid, i, j)
for row in grid:
    print("".join(row))