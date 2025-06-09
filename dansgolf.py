n,m,k=map(int, input().split())
activated = set()
res = 0
positions = set()
for _ in range(k):
    i, j = map(int, input().split())
    if (i - j - 1, 0) in activated:
        pass
    else:
        activated.add((i - j- 1, 0))

print(len(activated))