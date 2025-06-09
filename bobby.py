from math import comb


n = int(input())

def bin(n, k, p):
    res = 0
    for i in range(k, n+1):
        res += comb(n, i) * (p) ** i * (1-p)**(n-i)
    return res


for i in range(n):
    R, S, X, Y, W = map(int, input().split(" "))
    p = (S -R  + 1)/S
    prob = bin(Y, X, p)
    if W*prob > 1:
        print("yes")
    else:
        print("no")