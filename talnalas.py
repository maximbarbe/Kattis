from collections import deque



n,m=map(int, input().split())
src = input()
dest = input()
lucky = dict()
for i in range(m):
    lucky[input()] = True
lucky[dest] = True
visited = dict()

predecessors = dict()
predecessors[src] = None
q = deque([src])
while q:
    cur = q.popleft()
    if cur == dest:
        break
    
    visited[cur] = True
    digits = [*map(int, [char for char in cur])]
    for i in range(len(digits)):
        digits[i] = (digits[i] + 1)%10
        option1 = "".join(map(str, digits))
        digits[i] = (digits[i] - 2)%10
        option2 = "".join(map(str, digits))
        if visited.get(option1, False) == False and lucky.get(option1, False):
            q.append(option1)
            visited[option1] = True
            predecessors[option1] = cur
        if visited.get(option2, False) == False and lucky.get(option2, False):
            q.append(option2)
            visited[option2] = True
            predecessors[option2] = cur
        digits[i] = (digits[i] + 1)%10
else:
    print("Neibb")
    exit()
cur = dest
path = []
while cur != None:
    path.append(cur)
    cur = predecessors[cur]
path = path[::-1]
print(len(path) - 1)
for i in range(len(path)):
    print(path[i])