import heapq
from math import inf

#Greedy algorithm, dont know why it works but it does

n, x = map(int, input().split(" "))
names = []
for i in range(n):
    name, scale, const = input().split(" ")
    scale = int(scale)
    const = int(const)
    if scale == 0:
        priority = 0
    elif const == 0:
        priority = inf
    else:
        priority = scale / const
        
    names.append((priority, name))
    
heapq.heapify(names)
while len(names) != 0:
    name = heapq.heappop(names)
    print(name[1])