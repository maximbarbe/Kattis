from collections import deque
q = deque()
n, k = map(int, input().split())
vals = [*map(int, input().split())]
res = 0
for v in vals:
    if q:
        if v - q[0] >= k:
            q.popleft()
            q.append(v)
        else:
            q.append(v)
            res += 1
    else:
        q.append(v)
        res += 1
print(res)