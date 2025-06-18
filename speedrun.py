intervals = []
g, n = map(int, input().split(" "))

non_overlapping = 0
prev_end = 0
for i in range(n):
    start, end = map(int, input().split())
    intervals.append((start, end))
    
intervals.sort(key = lambda el:el[1])
for i in range(len(intervals)):
    if intervals[i][0] >= prev_end:
        non_overlapping += 1
        prev_end = intervals[i][1]
if non_overlapping >= g:
    print("YES")
else:
    print("NO")