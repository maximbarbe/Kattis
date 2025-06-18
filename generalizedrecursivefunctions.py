from functools import lru_cache
import sys

@lru_cache(sys.maxsize)
def f(x, y, c, d):
    if x > 0 and y > 0:
        s = 0
        for i in range(0, len(vals), 2):
            s += f(x - vals[i], y - vals[i + 1], c, d)
        return s + c
    else:
        return d
    
t = int(input())
for i in range(t):
    f.cache_clear()
    *vals, c, d = map(int, input().split())
    xy = [*map(int, input().split())]
    for j in range(0, len(xy), 2):
        print(f(xy[j], xy[j+1], c, d))
    print()