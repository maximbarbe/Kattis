from math import e


def cosh(x):
    return (pow(e, x) + pow(e, -x))/2

def sinh(x):
    return (pow(e, x) - pow(e, -x))/2

d, s = map(int, input().split(" "))
low = 0
high = 1000000
while True:
    a = (low + high)/2
    res = a * cosh(d/(2*a)) - a
    if abs(res - s) <= 0.00005:
        break
    else:
        if res < s:
            high = a
        else:
            low = a
res = 2 * a * sinh(d/(2*a))
print(res)