def prod(m1, m2):
    res = [[0 for i in range(len(m1))] for j in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1)):
            for k in range(len(m1)):
                res[i][j] += m1[i][k] * m2[k][j]
        res[i][j] %= m
    return res
def fast_exp(matrix, k):
    if k == 1:
        return matrix
    else:
        if k % 2 == 0:
            return prod(fast_exp(matrix, k//2), fast_exp(matrix, k//2))
        else:
            return prod(matrix, prod(fast_exp(matrix, k//2), fast_exp(matrix, k//2)))


n, m, k = map(int, input().split())

matrix = []
for i in range(n):
    row = [*map(int, input().split())]
    matrix.append(row)
input()
start_states = [*map(int, input().split())]
input()
end_states = [*map(int, input().split())]  
if k == 0:
    res = 0
    for s in start_states:
        for v in end_states:
            if s == v:
                res += 1
    print(res%m)
    exit()
state_matrix = fast_exp(matrix, k)
res = 0
for s in start_states:
    for v in end_states:
        res += state_matrix[s][v]
print(res%m)