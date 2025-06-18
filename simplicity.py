import heapq
from collections import defaultdict

frequencies = defaultdict(lambda:0)

string = input()
for i in range(len(string)):
    frequencies[string[i]] += 1
heap = [val for val in frequencies.values()]
res = 0
heapq.heapify(heap)
while len(heap) > 2:
    res += heapq.heappop(heap)
print(res)