import heapq
n,t = map(int, input().split())
data=  []
times = [[] for i in range(t+ 1)]
heap = []
res = 0
for i in range(n):
    ci, ti = map(int, input().split())
    times[ti].append(ci)
for i in range(t-1, -1, -1):
    for el in times[i]:
        heapq.heappush(heap, -el)
    if heap:
        res += -heapq.heappop(heap)
print(res)
