def generate(grid, i, j):
    if i + 1 == len(grid):
        return
    else:
        if grid[i + 1][j] == "O":
            grid[i + 1][j] = "~"
            generate(grid, i + 1, j)
        elif grid[i + 1][j] == "~":
            return
        else:
            if j + 1 != len(grid[i]) and grid[i][j + 1] == "O":
                grid[i][j + 1] = "~"
                generate(grid, i, j+1)
            if j - 1 != -1 and grid[i][j - 1] == "O":
                grid[i][j - 1] = "~"
                generate(grid, i, j-1)


n, m, k = map(int, input().split())
sources = [*map(int, input().split())]
grid = []
for i in range(n):
    grid.append([char for char in input()])
for src in sources:
    grid[0][src] = "~"
    generate(grid, 0, src)
for row in grid:
    print("".join(row))