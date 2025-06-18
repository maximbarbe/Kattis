from collections import deque

n,m = map(int, input().split())
values = [*map(int, input().split())]
values.sort()
q = deque(values)
res = 0
while q:
    if len(q) == 1:
        q.pop()
        res += 1
    else:
        if q[0] + q[-1] <= m:
            res += 1
            q.popleft()
            q.pop()
        else:
            q.pop()
            res += 1


print(res)