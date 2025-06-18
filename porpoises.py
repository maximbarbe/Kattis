# This is just the fibonacci sequence for very large numbers
# We just have to do the matrix squaring algorithm mod 10**9 so we dont have TLE


MOD = 10**9
def mult(A, B):
    res = [[(A[0][0] * B[0][0] + A[0][1] * B[1][0])% MOD, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
           [(A[1][0] * B[0][0] + A[1][1] * B[1][0])% MOD, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]]
    return res


# Basic fast matrix exponentiation
def expMatrix(matrix, year):
    if year == 1:
        return matrix
    else:
        temp = expMatrix(matrix, year//2)
        if year % 2== 0:
            return mult(temp, temp)
        else:
            return mult(mult(temp, temp), matrix)


fib = [[1, 1],
       [1, 0]]
n = int(input())
for i in range(n):
    k, year = map(int, input().split())
    res = expMatrix(fib, year)
    print(f"{k} {res[0][1]}")