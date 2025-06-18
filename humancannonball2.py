from math import cos, sin, radians
n = int(input())
for i in range(n):
    v_0, theta, x_1, h_1, h_2 = map(float, input().split(" "))
    angle = radians(theta)
    t = x_1/(v_0 * cos(angle))
    y_t = v_0 * t * sin(angle) - 1/2 * 9.81 * t ** 2
    if y_t - h_1 > 1 and h_2 - y_t > 1:
        print("Safe")
    else:
        print("Not Safe")