from math import gcd


def base3(n):
    res = []
    while n != 0:
        res.append(n%3)
        n //=3
        
    return [0] if len(res) == 0 else "".join(map(str, res[::-1]))


words = input().split()
for w in words:
    vals = [*map(ord, w)]
    g = gcd(*vals)
    for i in range(len(vals)):
        vals[i] = vals[i]//g
    print(g)
    print(*map(base3, vals))