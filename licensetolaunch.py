from math import inf
n = int(input())
min = inf
min_idx = 0
data = list(map(int, input().split(" ")))
for i in range(len(data)):
    if data[i] < min:
        min_idx = i
        min = data[i]
print(min_idx)