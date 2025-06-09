import itertools
t = int(input())
for i in range(t):
    trees = []
    n, A,B,C,D,x0,y0, M = map(int, input().split(" "))
    X, Y = x0, y0
    trees.append((X, Y))
    for j in range(1, n):
        X = (A * X + B)%M
        Y = (C * Y + D)%M
        trees.append((X, Y))
    res = 0
    for v1, v2, v3 in itertools.combinations(trees, 3):
        if (v1[0] + v2[0] + v3[0]) % 3 == 0 and (v1[1] + v2[1] + v3[1])%3 == 0:
            res += 1
    print(f"Case #{i + 1}: {res}")