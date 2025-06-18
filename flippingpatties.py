# Interval overlapping
from math import ceil

times = [0 for i in range(43201)]
n = int(input())
for i in range(n):
    di, ti = map(int, input().split(" "))
    
    times[ti - 2 * di] += 1
    times[ti - di] += 1
    times[ti] += 1
print(ceil(max(times)/2))