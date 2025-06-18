n,m,s,t = map(int, input().split())



def matmul(a, b):
    res = [[0 for i in range(len(a))] for j in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a)):
            for k in range(len(a)):
                res[i][j] += a[i][k] * b[k][j]
    return res

def mat_exp(power, mat):
    if power == 1:
        return mat
    else:
        if power % 2 == 0:
            return matmul(mat_exp(power//2, mat), mat_exp(power//2, mat))
        else:
            return matmul(mat, matmul(mat_exp(power//2, mat), mat_exp(power//2, mat)))



grid = [[0 for i in range(n)] for j in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    grid[a][b] = 1
    grid[b][a] = 1


if t == 0:
    print(1)
else:
    grid = mat_exp(t, grid)
    res = 0
    for i in range(n):
        res += grid[s][i]
    print(res)