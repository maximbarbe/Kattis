n = int(input())
intervals = []
for i in range(n):
    start, finish = map(int, input().split(" "))
    intervals.append((start, finish))
intervals.sort(key=lambda el:el[1])
res = [intervals[0]]
for i in range(1, len(intervals)):
    if intervals[i][0] >= res[-1][1]:
        res.append(intervals[i])
        
print(len(res))