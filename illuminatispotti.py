n = int(input())
grid = []
for i in range(n):
    grid.append([*map(int, input().split())])
    
res = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        if grid[i][j] == 1:
            for k in range(j + 1, n):
                if grid[j][k] == 1 and grid[k][i] == 1:
                    res += 1
print(res)