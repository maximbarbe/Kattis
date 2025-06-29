from collections import defaultdict, deque
import sys



n = int(input())

in_degrees = [0]*n
edges = [[] for i in range(n)]
for i in range(n):
    k, *dest = map(int, input().split())
    for v in dest:
        in_degrees[i] += 1
        edges[v-1].append(i)

next_level = []
levels = []
for i in range(n):
    if in_degrees[i] == 0:
        next_level.append(i)
        
while next_level != []:
    cur = next_level
    levels.append(cur)
    next_level = []
    for v in cur:
        for dest in edges[v]:
            in_degrees[dest] -= 1
            if in_degrees[dest] == 0:
                next_level.append(dest)
    
for i in range(n):
    if in_degrees[i] != 0:
        print("Omogulegt!")
        exit()
print("Mogulegt!")
print(len(levels))
for i in range(len(levels)):
    print(len(levels[i]), *map(lambda el:int(el) + 1, levels[i]))

        

