from math import floor, ceil

m, a, b, c = map(int, input().split(" "))
if (a + b + c)/2  <= m:
    print("possible")
else:
    print("impossible")