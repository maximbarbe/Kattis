from collections import defaultdict, deque


n, m = map(int, input().split())
pa, pb = map(int, input().split())

visited_alice = defaultdict(lambda:False)
visited_bob = defaultdict(lambda:False)
distance_alice = defaultdict(lambda:10_001)
distance_bob = defaultdict(lambda:10_001)
edges = defaultdict(lambda:[])
for i in range(m):
    p1, p2 = map(int, input().split())
    edges[p1].append(p2)
    edges[p2].append(p1)
    
distance_alice[pa] = 0
visited_alice[pa] = True
visited_bob[pb] = True
distance_bob[pb] = 0
q = deque([(pa, 0, True), (pb, 0, False)])
while q:
    cur, d, alice = q.popleft()
    for dest in edges[cur]:
        if alice:
            
            if not visited_alice[dest]:
                visited_alice[dest] = True
                distance_alice[dest] = d + 1
                q.append((dest, d + 1, True))
        else:
            if not visited_bob[dest]:
                visited_bob[dest] = True
                distance_bob[dest] = d + 1
                q.append((dest, d + 1, False))
res = 10_001
for i in range(n):
    res = min(res, max(distance_alice[i], distance_bob[i]))
print(res)
