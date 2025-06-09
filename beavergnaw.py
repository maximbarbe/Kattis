from math import pi
while True:
    D, V = map(int, input().split(" "))
    if D == V == 0:
        break
    V_t = (pi * D**3)/4
    top = V_t - (D**3 * pi)/12 - V
    bottom =  pi/6
    d = (top/bottom)**(1/3)
    print(d)