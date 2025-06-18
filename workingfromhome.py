from math import ceil
baseline, p, n = map(int, input().split(" "))

prev = 0
res = 0
m = baseline
for i in range(n):
    worked = int(input())
    m = ceil(baseline - (prev * p )/100)
    if worked >= m:
        res += 1
    prev = worked - m
print(res)