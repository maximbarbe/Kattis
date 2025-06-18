from collections import defaultdict, deque
import sys

def parcourir(x, y, cache, moves_cache):

    queue = deque()
    queue.append((x, y, 0))
    while len(queue) != 0:
        cur = queue.popleft()
        cache[(cur[0], cur[1])] = True
        moves_cache[cur[2]].append((cur[0], cur[1]))
        for x, y in [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]:
            if 0 <= cur[0] + x <= 7 and 0 <= cur[1] + y <= 7 and not cache[(cur[0] + x, cur[1] + y)]:
                queue.append((cur[0] + x, cur[1] + y, cur[2] + 1))
                cache[(cur[0] + x, cur[1] + y)] = True

n = int(input())

for i in range(n):
    moves = defaultdict(lambda: [])
    visited = defaultdict(lambda: False)
    data = input()
    x = data[0]
    y = data[1]
    x = ord(x) - ord("a")
    y = int(y) - 1
    parcourir(x, y, visited, moves)
    res = []
    max_key = max(moves.keys())
    res.append(str(max_key))
    pos = moves[max_key]
    pos = list(sorted(pos, key=lambda x: x[1], reverse=True))
    for i in range(len(pos) - 1):
        for j in range(i + 1, len(pos)):
            if pos[i][1] == pos[j][1] and pos[i][0] > pos[j][0]:
                pos[j], pos[i] = pos[i], pos[j]
    for x, y in pos:
        res.append(f"{chr(ord('a') + x)}{y+1}")
    print(" ".join(res))