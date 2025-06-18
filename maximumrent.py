def f(a, alpha, b, beta):
    return a*(alpha + 1)+ b*(beta + 1)
    
a,b = map(int, input().split())
m,s= map(int, input().split())
col = [m-2, s-3]
rows = [[1, 2], [1, 1], [1, 0], [0, -1]]
res = 0
for i in range(len(rows) - 1):
    for j in range(i +1, len(rows)):
        matrix = [[rows[i][0], rows[j][0]], [rows[i][1], rows[j][1]]]
        det = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
        if det != 0:
            inverse = [[1/det * matrix[1][1], 1/det * -matrix[0][1]],
                       [1/det * -matrix[1][0], 1/det * matrix[0][0]]]
            sol = [inverse[0][0] * col[0] + inverse[0][1] * col[1], inverse[1][0] * col[0] + inverse[1][1] * col[1]]
            if all([val >= 0 for val in sol]):
                solution = [0] * 4
                solution[i] = sol[0]
                solution[j] = sol[1]
                res = max(res, f(a, solution[0], b, solution[1]))
    
print(int(res))