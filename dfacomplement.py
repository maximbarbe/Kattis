from collections import defaultdict, deque


def res(init, accept, transition):
    visited = set()
    q = deque([(init, 0)])
    while q:
        cur, moves = q.popleft()
        if cur in accept:
            return moves
        visited.add(cur)
        for t in transition[cur]:
            if not transition[cur][t] in visited:
                visited.add(transition[cur][t])
                q.append((transition[cur][t], moves + 1))

    
    return moves
    


n,c,s,f = map(int, input().split())
s -= 1
a = input()
alphabet = {a[i]:i for i in range(len(a))}
accept = set([*map(lambda el: int(el)-1, input().split())])
comp_accept = []
transitions=[]

for i in range(1, n + 1):
    if i -1 not in accept:
        comp_accept.append(i) 

print(n,c,s + 1,len(comp_accept))
print(a)
print(*comp_accept)
for i in range(n):
    print(input())