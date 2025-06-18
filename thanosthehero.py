n = int(input())
vals = [*map(int, input().split())]
res = 0
for i in range(len(vals) - 2, -1, -1):
    if vals[i] < vals[i + 1]:
        continue
    else:
        diff = vals[i] - vals[i + 1] + 1
        res += diff
        vals[i] -= diff
        if vals[i] < 0:
            print(1)
            exit()
print(res)