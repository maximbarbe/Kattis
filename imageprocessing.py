n, m, h, w = map(int, input().split(" "))
matrix = []
kernel = []
for i in range(n):
    matrix.append([*map(int, input().split(" "))])
for i in range(h):
    kernel.append([*map(int, input().split(" "))])
for i in range(len(kernel)//2):
    kernel[i], kernel[- (i + 1)] = kernel[- (i + 1)], kernel[i]
for i in range(len(kernel)):
    for j in range(len(kernel[i]) //2):
        kernel[i][j], kernel[i][- (j + 1)] = kernel[i][- (j + 1)], kernel[i][j]
        
res = []
for i in range(len(matrix) - len(kernel) + 1):
    row = []
    for j in range(len(matrix[i]) - len(kernel[0]) + 1):
        cur = 0
        for k in range(len(kernel)):
            for l in range(len(kernel[0])):
                cur += kernel[k][l] * matrix[i+k][j + l]
        row.append(cur)
    res.append(row)
for row in res:
    print(" ".join(map(str, row)))