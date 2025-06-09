import sys
from collections import defaultdict
while True:
    n, m = map(int, sys.stdin.readline().split(" "))
    if n == m == 0:
        break
    res = 0
    jack = defaultdict(lambda: False)
    for i in range(n):
        jack[int(sys.stdin.readline())] = True
    for i in range(m):
        if jack[int(sys.stdin.readline())] == True:
            res += 1
    print(res)