import heapq
chosen = set()

n, k = map(int, input().split())
a_heap= []
d_heap = []
h_heap = []
for i in range(n):
    ai, di, hi = map(int, input().split())
    a_heap.append((-ai, i))
    d_heap.append((-di, i))
    h_heap.append((-hi, i))
heapq.heapify(a_heap)
heapq.heapify(d_heap)
heapq.heapify(h_heap)
for i in range(k):
    chosen.add(heapq.heappop(a_heap)[1])
    chosen.add(heapq.heappop(d_heap)[1])
    chosen.add(heapq.heappop(h_heap)[1])
print(len(chosen))