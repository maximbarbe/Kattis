import itertools
from math import inf
n = int(input())
data = []
for i in range(n):
    sour, bitter = map(int, input().split(" "))
    data.append((sour, bitter))
    
min_diff = inf

for i in range(1, n+1):
    el = itertools.combinations(data, i)
    for chosen in el:
        sumn = 0
        prod = 1
        for k in chosen:
            sumn += k[1]
            prod *= k[0]
        if abs(sumn - prod) < min_diff:
            min_diff = abs(sumn - prod)
print(min_diff)