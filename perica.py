from math import comb
n, k = map(int, input().split())
vals = [*map(int, input().split())]
vals.sort()
res = 0
for i in range(len(vals) - 1, -1, -1):
    # Since they are sorted, we know that vals[i] is going to be the greatest value.
    # We then have to choose k - 1 values from the remaining i smaller or equal values
    res += vals[i] * (comb(i, k - 1))
print(res % 1_000_000_007)