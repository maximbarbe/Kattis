from math import sqrt, floor

# Pseudo-code from here: https://cs.stackexchange.com/questions/4998/is-there-a-olog-n-algorithm-for-matrix-exponentiation

def matrix_power(matrix, power):
    if power == 1:
        return matrix
    else:
        P = matrix_power(matrix, floor(power/2))
        if power % 2 == 0:
            return mult(P, P)
        else:
            return mult(mult(P, P), matrix)


def mult(A, B):
    # Assumes A and B are 2x2 matrices
    res = [[(A[0][0]*B[0][0]+A[0][1] * B[1][0])%mod, (A[0][0]*B[0][1] + A[0][1]*B[1][1])%mod],
         [(A[1][0]*B[0][0]+A[1][1] * B[1][0])%mod, (A[1][0]*B[0][1] + A[1][1]*B[1][1])%mod]]
    return res


mod = 10**9 +7
a, b = map(int, input().split())
n = int(input())
if n == 0:
    print(a, b)
    exit()



fib = [[1, 1],
       [1, 0]]

fib_res = matrix_power(fib, 2*n)

denom_a = (fib_res[1][1]*a + fib_res[1][0]*b)%mod
denom_b = (fib_res[0][1]*a + fib_res[0][0]*b)%mod
print(denom_a, denom_b)