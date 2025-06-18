import sys
from collections import defaultdict
from math import sqrt, ceil
for line in sys.stdin:
    factors = defaultdict(lambda:0)
    n = int(line)
    temp = n
    while n % 2 == 0:
        n //= 2
        factors[2] += 1
    for i in range(3, ceil(sqrt(n)) + 1, 2):
        while n % i == 0:
            factors[i] += 1
            n //= i
        if n < i:
            break
    if n != 1:
        factors[n] += 1
    res = 1
    for key, val in factors.items():
        res *= pow(val, key)
    print(temp, res)