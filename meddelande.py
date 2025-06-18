n, m = map(lambda x: int(x), input().split(" "))

grid = []
for i in range(n):
    grid.append([*input()])
res = ""
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] != ".":
            res += grid[i][j]
print(res)