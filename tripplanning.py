from collections import defaultdict
from math import inf

edges = defaultdict(lambda: defaultdict(lambda: inf))
n, m = map(int, input().split(" "))
for i in range(1, m+1):
    src, dest = map(int, input().split(" "))
    edges[src][dest] = i
    edges[dest][src] = i
path = []
cur = 1
while True:
    if cur == n:
        break
    else:
        if edges[cur][cur + 1] != inf:
            path.append(edges[cur][cur + 1])
            cur += 1
        else:
            print("impossible")
            exit()
    
if edges[cur][1] != inf:
    path.append(edges[cur][1])
    for edge in path:
        print(edge)
    exit()
else:
    print("impossible")