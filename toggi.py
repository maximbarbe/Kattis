from math import log10


def f(x):
    return (x * log10(x))/(10**6)

c = int(input())
l, r = 1, 10**20


while l < r:
    if r - l == 1:
        if f(r) <= c:
            print(r)
        else:
            print(l)
        exit()
    m = (l+r)//2
    if f(m) == c:
        print(m)
        exit()
    elif f(m) < c:
        l = m
    else:
        r = m - 1
print(l)