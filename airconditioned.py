n = int(input())
vals = []
for i in range(n):
    start, end = map(int, input().split())
    vals.append((start, end))
vals.sort(key=lambda el:(el[1]))
prev_end = -1
res = 0
for i in range(len(vals)):
    if vals[i][0] > prev_end:
        res += 1
        prev_end = vals[i][1]
print(res)
