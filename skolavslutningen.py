from collections import defaultdict


n, m, k = map(int, input().split(" "))

colors = defaultdict(lambda: False)
grid = []
for i in range(n):
    grid.append(input())

res = 0
for j in range(m):
    seen = set()
    add_color = True
    for i in range(n):
        if colors[grid[i][j]] == True:
            add_color = False
        seen.add(grid[i][j])
    if add_color:
        res += 1
    for el in seen:
        colors[el] = True
        
print(res)