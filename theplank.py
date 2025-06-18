n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print(2)
elif n == 3: print(4)
else:
    dp = [1, 2, 4]
    dp += [0 for i in range(n - 3)]
    for i in range(3, len(dp)):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    print(dp[-1])
