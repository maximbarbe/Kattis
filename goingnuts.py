n = int(input())
vals = [2**i for i in range(21)]
steps = 0
for i in range(len(vals) - 1, -1, -1):
    while vals[i] <= n:
        n -= vals[i]
        steps += 1
print(steps)