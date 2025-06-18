n = int(input())
mod = 10**9 + 7
prod = 1
for i in range(n):
    prod = (int(input())%mod * prod%mod)%mod
print(prod)