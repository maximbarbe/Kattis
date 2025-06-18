from math import pi, sin
def get_radius(n, s):
    return s / (2 * sin((pi/n)))

def get_area(n, r):
    return 1/2 * n * r**2 * sin((2 * pi)/n)

m = int(input())
for i in range(m):
    n, l, d, g = map(int, input().split(" "))
    initial_radius = get_radius(n, l)
    area = get_area(n, initial_radius)
    # Source: https://math.stackexchange.com/questions/2004162/area-of-shape-with-a-fixed-offset-around-the-perimeter
    # Author of the comment: https://math.stackexchange.com/users/35416/mvg
    p = n * l
    w = d* g
    print(area + p * w + pi * w**2)