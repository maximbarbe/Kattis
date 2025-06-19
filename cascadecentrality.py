from collections import defaultdict, deque



def get_product(src, dest):
    q = deque([(src, 1)])
    visited = defaultdict(lambda:False)
    visited[src] = True
    while q:
        cur, prod = q.popleft()
        if cur == dest:
            return prod
        for d in edges[cur]:
            if not visited[d]:
                q.append((d, prod*degrees[d]))
                visited[d] = True
    else:
        return None

n = int(input())

edges = defaultdict(lambda:[])
degrees = defaultdict(lambda:0)
for i in range(n-1):
    u,v=map(lambda el:int(el) - 1, input().split())
    edges[u].append(v)
    edges[v].append(u)
    degrees[u] += 1
    degrees[v] += 1
cascade = dict()
for i in range(n):
    cascade[i] = 1
    temp = 0
    for j in range(n):
        if i == j:
            continue
        res = get_product(i, j)
        if res != None:
            temp += 1/res
    cascade[i] += temp

res = 0
for val in cascade.values():
    res += val
print(res/n)