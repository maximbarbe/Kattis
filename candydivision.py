from math import sqrt, floor
n = int(input())
if n == 1:
    print(1)
    exit()
res = set([0, n-1])
for i in range(2, floor(sqrt(n)) + 1):
    if n % i == 0:
        res.add(i - 1)
        res.add(n//i - 1)
res = sorted(res)

print(*res)