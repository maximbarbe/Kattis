from math import comb
n = int(input())
if n == 4:
    print(4)
else:
    print(4*comb(n//4, 2) + 4)