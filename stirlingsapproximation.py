from math import log, pi, e
from functools import lru_cache

@lru_cache
def f(n):
    if n == 1: return 1.084437551419227546611577313
    numerator = 0
    for i in range(1, n+1):
        numerator += log(i)
    denominator = (log(2*pi) + log(n))/2 + n*log(n) - n
    return e**(numerator- denominator)

while n:= input():
    if n == "0":
        exit()
    n = int(n)
    print(f(n))