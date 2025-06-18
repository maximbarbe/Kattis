import sys
from math import inf
from collections import defaultdict, deque


for line in sys.stdin:
    
    cache = defaultdict(lambda: False)
    heads, tails = map(int, line.strip("\n").split(" "))
    if heads == tails == 0:
        break
    moves = deque([(heads, tails, 0)])
    if tails == 0:
        print(-1)
    while True:
        cur = moves.popleft()
        cache[(cur[0], cur[1])] = True
        if cur[0] == cur[1] == 0:
            print(cur[2])
            break
        else:
            if cur[1] - 1 >= 0:
                if not cache[(cur[0], cur[1] + 1)]:
                    cache[(cur[0], cur[1] + 1)] = True
                    moves.append((cur[0], cur[1] + 1, cur[2] + 1))
            if cur[1] - 2 >= 0:
                
                if not cache[(cur[0] + 1, cur[1] - 2)]:
                    cache[(cur[0] + 1, cur[1] - 2)] = True
                    moves.append((cur[0] + 1, cur[1] - 2, cur[2] + 1))
            if cur[0] -2 >= 0:
                if not cache[(cur[0] - 2, cur[1])]:
                    cache[(cur[0] - 2, cur[1])] = True
                    moves.append((cur[0] - 2, cur[1], cur[2] + 1))