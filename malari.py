n, m = map(int, input().split())
intervals = []
for i in range(m):
    s, e = map(int, input().split())
    intervals.append((s, e))
intervals.sort(key=lambda el:(el[0], el[1]))
res = [intervals[0]]
for i in range(1, len(intervals)):
    if intervals[i][0] > res[-1][1]:
        res.append(intervals[i])
    else:
        res[-1] = (res[-1][0], max(res[-1][1], intervals[i][1]))
r = 0
for a, b in res:
    r += b-a + 1
print(r)
if r > n/2:
    print("The Mexicans took our jobs! Sad!")
else:
    print("The Mexicans are Lazy! Sad!")