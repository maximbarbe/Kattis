from bisect import bisect_left
from math import dist
d = []
for i in range(int(input())):
    x,y = map(int, input().split())
    d.append(dist((0,0), (x,y)))
d.sort()
for i in range(int(input())):
    t = int(int(input()))
    idx = bisect_left(d, t)
    if idx == 0 and d[idx] <= t:
        print(1)
    elif idx == len(d):
        print(len(d))
    else:
        print(idx)