from math import pi, cos, sin, floor

h,v=map(int,input().split())
if 0 <= v <= 180:
    print("safe")
else:
    theta = (v / 360) * 2 * pi
    dx = cos(theta)
    dy = sin(theta)
    print(floor(abs(h/dy)))