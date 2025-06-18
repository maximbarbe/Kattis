def multiply_matrix(m1, m2):
    res = [[0 for i in range(len(m1))] for j in range(len(m2))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                res[i][j] += m1[i][k] * m2[k][j]
    return res
while True:
    n = int(input())
    if n == -1:
        break
    grid = []
    for i in range(n):
        grid.append(list(map(int, input().split(" "))))
    paths = multiply_matrix(grid, multiply_matrix(grid, grid))
    weak = []
    for i in range(n):
        if paths[i][i] == 0:
            weak.append(str(i))
    print(" ".join(weak))