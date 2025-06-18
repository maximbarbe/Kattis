n, m, k = map(int, input().split())
pos = dict()
for i in range(k):
    x, y = map(lambda el: int(el) - 1, input().split())
    pos[(x, y)] = True
    
for i in range(n):
    for j in range(m):
        if pos.get((i, j), False) == True:
            print("*", end="")
        else:
            print(".", end="")
    print()