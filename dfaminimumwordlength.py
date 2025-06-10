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
transition = defaultdict(lambda:defaultdict(lambda:None))
for i in range(n):
    transitions = [*map(int, input().split())]
    for j in range(len(transitions)):
        transition[i][a[j]] = transitions[j] - 1

print(res(s, accept, transition))