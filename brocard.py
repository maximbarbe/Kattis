from math import dist

n = int(input())
for i in range(n):
    k, ax, ay, bx, by, cx, cy = map(float, input().split())
    
    a = dist((bx, by), (cx, cy))
    b = dist((ax, ay), (cx, cy))
    c = dist((ax, ay), (bx, by))
    T = [c/b, a/c, b/a]
    x = (ax, ay)
    y = (bx, by)
    z = (cx, cy)
    # Source for the formula: https://www.desmos.com/calculator/yixs3e3cr3?lang=fr
    coords = (((a * T[0])/(a*T[0] + b*T[1] + c*T[2]))*x[0] + ((b * T[1])/(a*T[0] + b*T[1] + c*T[2]))*y[0] + ((c * T[2])/(a*T[0] + b*T[1] + c*T[2]))*z[0], ((a * T[0])/(a*T[0] + b*T[1] + c*T[2]))*x[1] + ((b * T[1])/(a*T[0] + b*T[1] + c*T[2]))*y[1] + ((c * T[2])/(a*T[0] + b*T[1] + c*T[2]))*z[1])
    print(k, coords[0], coords[1])