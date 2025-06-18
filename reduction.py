from collections import defaultdict
from functools import lru_cache

def get_minimum(n, m, a, b):
    res = 0
    while n != m:
        if n//2 >= m and b <= a*(n-n//2):
            res += b
            n //= 2
        else:
            res += (n-m)*a
            n = m
        
    return res    
        



n = int(input())
for i in range(n):
    n, m, l =map(int, input().split())
    costs = defaultdict(lambda:None)
    for j in range(l):
        name, rates = input().split(":")
        a,b = map(int, rates.split(","))
        costs[name] = get_minimum(n,m , a, b)
    data = []
    for k, v in costs.items():
        data.append((k, v))
    data.sort(key=lambda el:(el[1], el[0]))
    print("Case", i+1)
    for k, v in data:
        print(k, v)     