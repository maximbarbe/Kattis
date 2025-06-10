n, m = map(int, input().split(" "))
grid = []
res = 0
for i in range(n):
    grid.append(input())
    
for j in range(m):
    for i in range(n):
        if grid[i][j] == "$":
            break
    else:
        res += 1
print(res + 1)