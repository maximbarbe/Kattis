s1 = input()
s2 = input()

dp = [[0 for i in range(len(s1) + 1)] for j in range(len(s2) + 1)]

for i in range(len(s2) + 1):
    dp[i][-1] = len(s2) - i
    
for i in range(len(s1) + 1):
    dp[-1][i] = len(s1) - i

for i in range(len(s2) -1, -1, -1):
    for j in range(len(s1) - 1, -1, -1):
        if s2[i] == s1[j]:
            dp[i][j] = 1 + min(dp[i + 1][j + 1], dp[i + 1][j], dp[i][j + 1])
        else:
            dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1])
res = []
i = j = 0
while i != len(s2) and j != len(s1):
    if dp[i + 1][j] == dp[i][j] - 1:
        res.append(s2[i])
        i += 1
    elif dp[i][j + 1] == dp[i][j] - 1:
        res.append(s1[j])
        j += 1
    else:
        res.append(s1[j])
        i += 1
        j += 1
while i != len(s2):
    res.append(s2[i])
    i += 1
    
while j != len(s1):
    res.append(s1[j])
    j += 1
print("".join(res))