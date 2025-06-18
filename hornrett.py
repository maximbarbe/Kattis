from math import pi, atan2
vals=sorted([*map(int, input().split())])
a = vals[0]
b = vals[1]
c = vals[2]
if a ** 2 + b ** 2 == c**2:
    print((a*b)//2)
else:
    print(-1)