res = 0
MOD = 10**10
n = int(input())
for i in range(1, n+1):
    
    res += pow(i, i,MOD)
    res %= MOD
print(res)