from math import floor, ceil, sqrt, inf
from collections import defaultdict

n, m = map(int, input().split())
factors = defaultdict(lambda:0)
while n % 2 == 0:
    n //= 2
    factors[2] += 1

for i in range(3, ceil(sqrt(n))+1, 2):
    while n % i == 0:
        factors[i] += 1
        n //= i
    if n < i:
        break
    
if n != 1:
    factors[n] += 1
    
res = inf

for fact in factors.keys():
    cur = 0
    temp = fact
    while floor(m/temp) != 0:
        cur += floor(m/temp)
        temp *= fact
    res = min(res, cur//factors[fact])
print(res)