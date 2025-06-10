from math import sqrt, gcd
a,b,k = map(int, input().split())
limit = sqrt(k)
def euclid(a, b):
    if a <= limit and b <= limit:
        print(max(a, b), min(a, b))
        exit()
    if b == 0:
        return a
    return euclid(b, a%b)
euclid(a,b)