n = int(input())
res = []
grid = []
for i in range(n):
    grid.append([*map(int, input().split(" "))])

for i in range(n):
    cur = 0
    for j in range(n):
        cur = cur | grid[i][j]
    res.append(cur)
print(" ".join(map(str, res)))