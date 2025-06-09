from collections import defaultdict
import heapq

heap = []
frequencies = defaultdict(lambda: 0)
n = int(input())

for i in range(n):
    frequencies[input()] += 1

for key,val in frequencies.items():
    heapq.heappush(heap, (val, key))
    
first = heapq.heappop(heap)
min_freq = first[0]
print(first[1])
while heap != []:
    cur = heapq.heappop(heap)
    if cur[0] > min_freq:
        break
    else:
        print(cur[1])