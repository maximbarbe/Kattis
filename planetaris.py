n, a = map(int, input().split())

vals = [*map(int, input().split())]
vals.sort()
res = 0
for i in range(len(vals)):
    if vals[i] + 1 <= a:
        res += 1
        a -= vals[i] + 1
    else:
        break
print(res)