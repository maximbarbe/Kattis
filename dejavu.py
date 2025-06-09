from collections import defaultdict
from math import comb


res = 0
n = int(input())
x_values = defaultdict(lambda:[])
y_values = defaultdict(lambda:[])
points = []
for i in range(n):
    x, y = map(int, input().split())
    x_values[x].append((x, y))
    y_values[y].append((x, y))
    points.append((x, y))

res = 0
for x, y in points:
    res += (len(x_values[x]) - 1) * (len(y_values[y]) - 1)
print(res)