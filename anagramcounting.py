from math import factorial
import sys
from collections import defaultdict
for line in sys.stdin:
    letters = defaultdict(lambda:0)
    line = line.rstrip()
    for i in range(len(line)):
        letters[line[i]] += 1
    res = factorial(len(line))
    for val in letters.values():
        res //= factorial(val)
    print(res)