from math import pi
R, C = map(int, input().split(" "))
cheese_area = pi * (R-C)**2
pizza_area = pi * R**2
print(cheese_area/pizza_area * 100)