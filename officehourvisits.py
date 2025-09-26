
intervals = []

t = int(input())

for i in range(t):
    start, end = map(int, input().split())
    intervals.append((start, end))

intervals.sort(key=lambda el:(el[1], el[0]))
res = 0
prev = 0
for s, e in intervals:
    if s >= prev:
        res += 1
        prev = e
print(res)