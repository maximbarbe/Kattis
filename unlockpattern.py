from collections import defaultdict
from math import dist
dict = defaultdict()
grid = []
for i in range(3):
    grid.append(list(map(int, input().split(" "))))
    
for i in range(3):
    for j in range(3):
        dict[grid[i][j]]  = (i, j)

res = 0
cur = 1
while cur != 9:
    first = dict[cur]
    second = dict[cur + 1]
    res += dist(first, second)
    cur += 1
print(res)