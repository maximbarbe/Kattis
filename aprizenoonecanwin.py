from math import floor
n, max_cost = map(int, input().split(" "))

vals = [*map(int, input().split(" "))]
res = 0
vals.sort()

for i in range(1, len(vals)):
    if vals[i] + vals[i - 1] <= max_cost:
        res += 1
print(res + 1)