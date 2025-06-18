from math import comb
t = int(input())
for i in range(t):
    n,k = map(int, input().split())
    print(comb(n, k-1))