from math import sin, ceil, radians
h, deg = map(int, input().split(" "))
print(ceil(h/sin(radians(deg))))