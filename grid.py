import heapq
from collections import deque
from math import inf

heap = []
n, m = map(int, input().split(" "))
grid = []
for i in range(n):
    grid.append([*map(int, [*input()])])
visited = [False for i in range(n*m)]

visited[0] = True
q = deque()
q.append((0, 0, 0))



while len(q) != 0:
    cur_dist, x, y = q.popleft()
    if x == n - 1 and y == m - 1:
        print(cur_dist)
        exit()
    for x1, y1 in [(0, grid[x][y]), (grid[x][y], 0), (-grid[x][y], 0), (0, -grid[x][y])]:
        if x1 + x >= 0 and x1 + x < n and y1 + y >= 0 and y1 + y < m and visited[(x1+x)*m + y1 + y] == False:
            visited[(x1+x)*m + y1 + y] = True
            q.append((cur_dist + 1, x1 + x, y1 + y))
    
else:
    print(-1)