from collections import deque 
from itertools import product

m,n,s=map(int,input().split())
pairs = []
for i in range(n):
    a,b = map(int, input().split())
    pairs.append((a,b))
q = deque([(s, 0)])
seen = {s}
while q:
    cur, moves = q.popleft()
    if cur == 0:
        print(moves)
        exit()
    for a,b in pairs:
        si = (cur * a + b)%m
        if si not in seen:
            seen.add(si)
            q.append((si, moves + 1))
else:
    print(-1)