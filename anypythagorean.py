from math import sqrt

n = int(input())
for a in range(1, n+1):
    for b in range(a, n+1):
        if a + 2*b >= n:
            break
        else:
            if a + b + sqrt(a**2 + b**2) == n:
                print(*sorted([a, b]), int(sqrt(a**2 + b**2)))
                exit()
else:
    print(0, 0, 0)