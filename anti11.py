# Dynamic programming approach
# dp[n][0] = dp[n - 1][0] + dp[n -1][1] since if we add a 0 at the end of the binary string then no 11 have been made
# dp[n][1] = dp[n- 1][0] since the only way to not make a substring 11 is to add a 1 after a 0

t = int(input())
for i in range(t):
    n = int(input())
    dp = [[0 for i in range(2)] for j in range(n)]
    dp[0][0] = 1
    dp[0][1] = 1
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
        dp[i][1] = dp[i - 1][0]
        
    print((sum(dp[-1]))%(10**9 + 7))