R, C = map(int, input().split(" "))
grid = []
res = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0
}
for i in range(R):
    grid.append(input())
    
for i in range(R - 1):
    for j in range(C - 1):
        if grid[i][j] == "#" or grid[i + 1][j] == "#" or grid[i][j + 1] == "#" or grid[i + 1][j + 1] == "#":
            continue
        else:
            cars = 0
            if grid[i][j] == "X":
                cars += 1
            if grid[i + 1][j] == "X":
                cars += 1
            if grid[i][j + 1] == "X":
                cars += 1
            if grid[i + 1][j + 1] == "X":
                cars += 1
            res[cars] += 1
for key in res.keys():
    print(res[key])