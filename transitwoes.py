s, t, n = map(int, input().split(" "))
walk_times = list(map(int, input().split(" ")))
cur = 0
bus_times = list(map(int, input().split(" ")))
intervals = list(map(int, input().split(" ")))
for i in range(len(intervals)):
    cur += walk_times[i]
    if cur % intervals[i] == 0:
        cur += bus_times[i]
    else:
        while cur % intervals[i] != 0:
            cur += 1
        cur += bus_times[i]
    
if cur + walk_times[-1] > t:
    print("no")
else:
    print("yes")