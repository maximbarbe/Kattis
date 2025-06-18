from math import comb
from collections import defaultdict

n, div = map(int, input().split())

results = defaultdict(lambda:0)
vals = [*map(int, input().split())]
for i in range(n):
    results[vals[i]//div] += 1
    
res = 0
for val in results.values():
    res += comb(val, 2)
print(res)