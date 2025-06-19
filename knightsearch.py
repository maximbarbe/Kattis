from collections import defaultdict

def dfs(i, j, s, idx):
    if idx == len(s):
        print("YES")
        exit()
    else:
        for x, y in [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]:
            if 0 <= i + x < n and 0 <= y + j < n and grid[i+x][y+j] == s[idx]:
                dfs(i + x, y+j, s, idx + 1)

s = "ICPCASIASG"
n = int(input())
grid = input()
grid = [grid[i:i+n] for i in range(0,len(grid), n)]
for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j]==s[0]:
            dfs(i, j, s, 1)
else:
    print("NO")