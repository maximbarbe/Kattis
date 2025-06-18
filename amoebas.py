from collections import defaultdict, deque


def bfs(pos, visited):
    queue = deque()
    queue.append(pos)
    while len(queue) != 0:
        cur = queue.pop()
        visited[cur] = True
        for x, y in [(1, 0), (1, 1), (1,  -1), (0, 1), (0,  -1), (-1,1), (-1,-1), (-1, 0)]:
            if visited[(cur[0] + x, cur[1] + y)]  == False:
                queue.append((cur[0] + x, cur[1] + y))
                visited[(cur[0] + x, cur[1] + y)] = True
    return

n, m = map(int, input().split(" "))

visited = defaultdict(lambda: None)

for i in range(n):
    row = input()
    for j in range(len(row)):
        if row[j] == "#":
            visited[(i, j)] = False
        
    
res = 0
to_check = [(key, val) for key, val in visited.items()]
for key, val in to_check:
    if visited[key] == False:
        res += 1
        bfs(key, visited)
print(res)