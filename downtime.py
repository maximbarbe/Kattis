from collections import deque

servers=  deque()
n, k = map(int, input().split())
res = 0
for i in range(n):
    timestamp = int(input())
    while servers and timestamp - servers[0] >= 1000:
        servers.popleft()
    servers.append(timestamp)
    if len(servers) % k == 0:
        res = max(res, len(servers) //k)
    else:
        res = max(res, len(servers) //k + 1)
print(res)