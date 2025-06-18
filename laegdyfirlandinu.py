n, m = map(int, input().split(" "))
grid = []
for i in range(n):
    grid.append(list(map(int, input().split(" "))))
    
for i in range(1, n - 1):
    for j in range(1, m - 1):
        if grid[i][j] < min([grid[i - 1][j], grid[i + 1][j], grid[i][j - 1], grid[i][j + 1]]):
            print("Jebb")
            exit()
print("Neibb")