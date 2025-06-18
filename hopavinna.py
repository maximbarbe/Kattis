n = int(input())

vals = [*map(int, input().split())]

    
# i = 0 == skipped
# i = 1 == not skipped
dp = [[0 for i in range(n + 2)] for j in range(2)]
for i in range(2, n + 2):
    # If I skipped this one, then I have to have done the previous one,
    dp[0][i] = dp[1][i - 1]
    # If I do this one, then I might have done the last one or I might not, we take the minimum
    dp[1][i] = vals[i - 2] + min(dp[0][i - 1], dp[1][i - 1])

print(min(dp[0][-1], dp[1][-1]))