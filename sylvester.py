from math import log2, ceil




def get_sign(i, j):
    if i == 0 and j == 0:
        return 1
    else:
        right = ceil(log2(j + 1))
        down = ceil(log2(i + 1))
        mat_exponent = max(right, down)
        middle = 2**(mat_exponent - 1)
        if i >= middle and j >= middle:
            if i > j:
                return -1 * get_sign(i - middle, j) 
            elif i < j:
                return -1 * get_sign(i, j - middle) 
            else:
                return -1 * get_sign(i - middle, j - middle)
        elif i >= middle:
                return 1 * get_sign(i - middle, j)
        elif j >= middle:
                return 1 * get_sign(i, j -middle)



t = int(input())
for i in range(t):
    n, x, y, w, h = map(int, input().split())
    for i in range(h):
        row = []
        for j in range(w):
            row.append(get_sign(y + i, x + j))
        print(*row)
    print()