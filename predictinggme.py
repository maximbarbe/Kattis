n = int(input())
dp = [0]*(n+3)
vals = [*map(int, input().split())] + [0, 0]
for i in range(n-1, -1, -1):
    for j in range(i + 1, n+1):
        dp[i] = max(dp[i], vals[j] - vals[i] + dp[j + 2], dp[j])
print(dp[0])