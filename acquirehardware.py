n, m = map(int, input().split())
grid = []
for i in range(n):
    grid.append(input())
dp = [[0 for i in range(m + 1)] for j in range(n+ 1)]
for i in range(n-1, -1, -1):
    for j in range(m - 1, -1, -1):
        if grid[i][j] == "I":
            dp[i][j] = 1 + max(dp[i + 1][j], dp[i][j + 1])
        else:
            dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
print(dp[0][0])