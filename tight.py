import sys
import decimal

decimal.getcontext().prec = 1000
# Can probably implement dynamic programming
# Count the number of ways we can end a string of length 1 that ends with 0-9
# Then for length n + 1, if ends with number j then the number before is in [j - 1, j, j+1]. So the number of ways is dp[i][j - 1] + dp[i][j] + dp[i][j + 1]
# We can then sum the last row and divide by the total number of strings in the alphabet
# dp[i][j] -> i = length of current string, j = last digit in string
# Initialise the dp table with the first row being all ones
for line in sys.stdin:
    k, n= map(int, line.split())
    dp = [[0 for i in range(k + 1)] for j in range(n)]
    for i in range(k + 1):
        dp[0][i] = 1
    
    for i in range(1, n):
        for j in range(k+1):
            if k == 0: 
                dp[i] = dp[i - 1]
            else:
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j + 1]
                elif j == k:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j -1]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j + 1] + dp[i - 1][j -1]
        
    print((decimal.Decimal(sum(dp[-1])/((k+1)**n)))*100)