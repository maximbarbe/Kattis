import sys
from math import log10, floor
from functools import lru_cache



res = [0 for i in range(1000000)]
cur = 0
for i in range(1, 1000001):
    cur += log10(i)
    res[i - 1] = floor(cur) + 1



for line in sys.stdin:
    n = int(line)
    if n == 0:
        print(1)
    else:
        print(res[n - 1])