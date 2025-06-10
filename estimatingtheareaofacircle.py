from math import pi
while True:
    r, m, c = map(float, input().split(" "))
    if r == m == c == 0:
        break
    square = 4*r**2
    print(f"{round(pi * r**2, 5)} {round((c/m) * square, 5)}")