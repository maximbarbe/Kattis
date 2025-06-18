from math import dist, sqrt, pi, acos, cos
import sys
for line in sys.stdin:
    r, x, y = map(float, line.strip("\n").split(" "))
    if dist((0, 0), (x, y)) > r:
        print("miss")
    else:
        # Formula for cord length: https://math.stackexchange.com/questions/3421969/find-the-shortest-length-of-a-chord-passing-through-a-point-inside-the-circle
        # Author: https://math.stackexchange.com/users/686284/quanto
        distance = dist((0, 0), (x, y))
        OC = 2 * sqrt(r**2 - distance**2)
        
        # Source for area: https://byjus.com/maths/area-segment-circle/
        theta = acos((r**2 + r**2 - OC**2)/(2 * r * r))
        OP = r*cos(theta/2)
        triangle = 1/2 * OP * OC
        small = theta/(2*pi) * pi * r**2 - triangle
        big = pi * r**2 - small
        print(f"{big} {small}")