from math import ceil

s = int(input())
p = int(input())
a = int(input())
b = int(input())
res = 0
while s/p <= 0.5:
    ratio_if_solve = (s+1)/p
    n = ceil(p/(p-s-1))
    ratio_if_add = (s+n)/(p+n)
    if ratio_if_add > 0.5:
        while (s + n - 1)/(p+n - 1) > 0.5 and n > 0:
            n -= 1
    if n * b < a:
        res += n * b
        s += n
        p += n
    else:
        res += a
        s += 1
print(res)