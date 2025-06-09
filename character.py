from math import comb


n = int(input())
if n in [0, 1]:
    print(0)
else:
    res = 0
    for i in range(2, n+1):
        res += comb(n, i)
    print(res)