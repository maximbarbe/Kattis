from math import sqrt
L, R = map(int, input().split(" "))
if sqrt(L ** 2 + L**2) <= 2 * R:
    print("fits")
else:
    print("nope")