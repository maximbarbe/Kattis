from math import sqrt

n = int(input())
for m in range(2, n):
    for j in range(2, m+1):
        if (m*n) % (j**2) == 0:
            break
    else:
        print(m)
        exit()