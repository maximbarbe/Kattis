from math import cos, ceil, pi

while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        print(1)
    elif n % 2 == 1:
        print(0)
    else:
        # Source of the formula for the solution: https://en.wikipedia.org/wiki/Domino_tiling
        res = 1
        for j in range(1, 3):
            for k in range(1, ceil(n/2) + 1):
                res *= 4*cos((pi*j)/(4))**2 + 4 *cos((pi*k)/(n+1)) ** 2
        print(round(res))