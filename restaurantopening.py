from math import inf

n, m = map(int, input().split(" "))
grid = []
for i in range(n):
    grid += [*map(int, input().split(" "))]
min_cost = inf
for i in range(len(grid)):
    cur = 0
    for j in range(len(grid)):
        if i != j:
            cur += grid[j] * (abs(j//m - i//m) + abs(j%m - i%m))
        
    if cur < min_cost:
        min_cost = cur
print(min_cost)