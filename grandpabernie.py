from collections import defaultdict
from bisect import insort_left


trips = defaultdict(lambda:[])


n = int(input())
for i in range(n):
    dest, year = input().split()
    year = int(year)
    insort_left(trips[dest], year)
    
q = int(input())
for i in range(q):
    dest, num = input().split()
    num = int(num)
    print(trips[dest][num - 1])