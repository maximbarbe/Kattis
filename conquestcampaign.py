from collections import deque, defaultdict


r, c, n = map(int, input().split(" "))
to_visit = r*c

q = deque()
in_queue = defaultdict(lambda:False)
visited = defaultdict(lambda:False)

for i in range(n):
    x, y = map(int, input().split(" "))
    if in_queue[(x-1,y-1)] == False:
        to_visit -= 1
    
    in_queue[(x-1,y-1)] = True
    q.append((x-1, y-1))
next_q = q
days = 1    
while to_visit != 0:
    
    if to_visit == 0:
        break
    q = next_q
    next_q = deque()
    while len(q) != 0:
        cur = q.popleft()
        visited[cur] = True
        for x, y in [(1,0), (-1,0), (0, 1), (0, -1)]:
            if not visited[(cur[0] + x, cur[1] + y)] and not in_queue[(cur[0] + x, cur[1] + y)] and cur[0] + x >= 0 and cur[0] + x < r and cur[1] + y >= 0 and cur[1] + y < c:
                to_visit -= 1
                in_queue[(cur[0] + x, cur[1] + y)] = True
                next_q.append((cur[0] + x, cur[1] + y))
    days += 1
print(days)