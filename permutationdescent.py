p = int(input())
for i in range(p):
    k, n, v = map(int, input().split(" "))
    dp = [[0 for i in range(v + 1)] for j in range(n+1)]
    
    # Source for solution:
    # https://en.wikipedia.org/wiki/Permutation
    # Source for recurrence formula: 
    # https://en.wikipedia.org/wiki/Eulerian_number
    for i in range(n + 1):
        dp[i][0] = 1
    for i in range(1, n+1):
        for j in range(1, v + 1):
            dp[i][j] = ((i - j)*dp[i - 1][j - 1]%1001113 + (j + 1)*dp[i - 1][j]%1001113)%1001113
    print(f"{k} {dp[-1][-1]%1001113}")