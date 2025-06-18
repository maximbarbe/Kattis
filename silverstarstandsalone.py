primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211]


n = int(input())
final = primes.index(n)
dp = [0] * (final +1)
dp[final] = 1
for i in range(final -1, -1, -1):
    for j in range(i+1, final+1):
        if primes[i] + 14 >= primes[j]:
            dp[i] += dp[j]
print(dp[0])