import datetime
from collections import deque
import heapq
epoch = datetime.datetime(year=2013, month=1,day=1, hour=0, minute=0)


n = int(input())
for i in range(n):
    k, cleaning = map(int, input().split())
    intervals = []
    cleaning *= 60
    for j in range(k):
        code, arr, arrt, dep, dept = input().split()
        arry, arrmonth, arrd = arr.split("-")
        arrh, arrm = arrt.split(":")
        depy, depmonth, depd = dep.split("-")
        deph, depm = dept.split(":")
        arrday = datetime.datetime(year=int(arry), month=int(arrmonth), day=int(arrd), hour=int(arrh), minute=int(arrm))
        depday = datetime.datetime(year=int(depy), month=int(depmonth), day=int(depd),hour=int(deph), minute=int(depm))
        intervals.append(((arrday-epoch).total_seconds(), (depday - epoch).total_seconds() + cleaning))
    intervals.sort(key=lambda el:(el[0], el[1]))
    first = intervals[0]
    processed = [first[1]]
    res = 1
    for i in range(1, len(intervals)):
        popped =False
        if processed and intervals[i][0] >= processed[0]:
            heapq.heappop(processed)
            popped = True
        if not popped:
            res += 1
        cur = intervals[i]
        heapq.heappush(processed, cur[1])
    print(res)