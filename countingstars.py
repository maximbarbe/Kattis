import sys
from collections import defaultdict, deque



def bfs(start, visited, pix):
    q = deque()
    in_queue = defaultdict(lambda:False)
    q.append(start)
    while len(q) != 0:
        cur = q.popleft()
        visited[cur] = True
        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_c = (cur[0] + x, cur[1] + y)
            if next_c in pix and not visited[next_c] and not in_queue[next_c]:
                q.append(next_c)
                in_queue[next_c] = True
                
    return
case_num = 0



while line := sys.stdin.readline():
    case_num += 1
    n, m = map(int, line.rstrip().split(" "))
    pix = set()
    visited = defaultdict(lambda: False)
    for i in range(n):
        line = sys.stdin.readline().rstrip()
        for j in range(len(line)):
            if line[j] == "-":
                pix.add((i, j))
    res = 0
    for el in pix:
        if not visited[el]:
            bfs(el, visited, pix)
            res += 1
    print(f"Case {case_num}: {res}")