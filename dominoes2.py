from collections import defaultdict, deque

t = int(input())
for i in range(t):
    n,m,l = map(int, input().split())
    fallen = [False for i in range(n+1)]
    
    edges = defaultdict(lambda:[])
    for i in range(m):
        src, dest = map(int, input().split())
        edges[src].append(dest)
    
    res = 0
    for i in range(l):
        src = int(input())
        if not fallen[src]:
            q = deque([src])
            while len(q) != 0:
                cur = q.popleft()
                fallen[cur] = True
                res += 1
                for d in edges[cur]:
                    if not fallen[d]:
                        q.append(d)
                        fallen[d] = True
                        
    print(res)