import sys

sys.setrecursionlimit(10**6)
def p(moves, strings, idx):
    print(strings[idx],end="")
    for i in moves[idx]:
        p(moves, strings, i)
n = int(input())
moved = [False]*n
moves = [[] for i in range(n)]
strings = []
for i in range(n):
    strings.append(input())
for i in range(n-1):
    src, dest = map(lambda el:int(el) - 1, input().split())
    moved[dest] = True
    moves[src].append(dest)
for i in range(n):
    if not moved[i]:
        p(moves, strings, i)
        print()
        exit()