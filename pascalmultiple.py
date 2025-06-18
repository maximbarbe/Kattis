from functools import lru_cache
from math import comb
import sys

n, k = map(int, input().split())
res = 0
dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
for i in range(n+1):
    dp[i][0] = 1
    
for i in range(1, n+1):
    if dp[i][0] % k == 0:
        res+= 1
    for j in range(1, i+1):
        dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
        if dp[i][j] % k == 0:
            res += 1
        

if k == 1:
    res += 1

print(res)