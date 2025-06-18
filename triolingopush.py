def mat_mul(a, b, mod):
    res = [[0 for i in range(3)] for j in range(3)]
    res[0][0] = (a[0][0] * b[0][0] + a[0][1]*b[1][0] + a[0][2]*b[2][0])%mod
    res[0][1] = (a[0][0] * b[0][1] + a[0][1]*b[1][1] + a[0][2]*b[2][1])%mod
    res[0][2] = (a[0][0] * b[0][2] + a[0][1]*b[1][2] + a[0][2]*b[2][2])%mod
    res[1][0] = (a[1][0] * b[0][0] + a[1][1]*b[1][0] + a[1][2]*b[2][0])%mod
    res[1][1] = (a[1][0] * b[0][1] + a[1][1]*b[1][1] + a[1][2]*b[2][1])%mod
    res[1][2] = (a[1][0] * b[0][2] + a[1][1]*b[1][2] + a[1][2]*b[2][2])%mod
    res[2][0] = (a[2][0] * b[0][0] + a[2][1]*b[1][0] + a[2][2]*b[2][0])%mod
    res[2][1] = (a[2][0] * b[0][1] + a[2][1]*b[1][1] + a[2][2]*b[2][1])%mod
    res[2][2] = (a[2][0] * b[0][2] + a[2][1]*b[1][2] + a[2][2]*b[2][2])%mod
    return res
    
def exp_mod(mat, e, mod):
    if e == 1:
        return mat 
    else:
        P = exp_mod(mat, e//2, mod)
        if e % 2 == 0:
            return mat_mul(P, P, mod)
        else:
            return mat_mul(mat, mat_mul(P, P, mod), mod)
    
    
MOD = 10**9 + 7




mat = [[1, 1, 1],
       [1, 0, 0],
       [0, 0, 1]]

n = int(input())
if n in [1, 2]:
    print((1, 2)[n-1])
    exit()
matrix = exp_mod(mat, n-2, MOD)

print((matrix[0][0] * 2 + matrix[0][1] + matrix[0][2])%MOD)