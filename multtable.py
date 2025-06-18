from math import floor, sqrt

n, m = map(int, input().split())
res = 0
for i in range(1, floor(sqrt(m)) + 1):
    if i > n:
        break
    if m % i == 0 and m//i <= n:
        if i *i == m:
            res += 1
        else:
            res += 2
print(res)