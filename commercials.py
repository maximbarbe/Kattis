n, p = map(int, input().split(" "))
vals = [*map(int, input().split(" "))]
dp = [0 for i in range(n+1)]
for i in range(1, n+1):
    dp[i] = max(0, dp[i-1] + vals[i-1] - p, vals[i-1] - p)
print(max(dp))