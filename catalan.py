from math import comb
from collections import defaultdict
import decimal
decimal.getcontext().prec = 10000
q = int(input())
res = [1]
# Recurrence relation found here https://en.wikipedia.org/wiki/Catalan_number
for i in range(1, 5001):
    res.append((2*(2*i - 1) * (res[i - 1]))//(i + 1))
for i in range(q):
    x = int(input())
    print(res[x])