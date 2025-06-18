from math import sqrt
x, y, x_1, y_1, x_2, y_2 = map(int, input().split(" "))
distance_x = 0
distance_y = 0
if x > x_2:
    distance_x = x_2 - x
elif x < x_1:
    distance_x = x_1 - x
if y > y_2:
    distance_y = y_2 - y
elif y < y_1:
    distance_y = y - y_1
print(sqrt(distance_x**2 + distance_y**2))