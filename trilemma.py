from math import acos, sqrt, degrees

def cross(x1, y1, x2, y2):
    return x1*y2 - x2*y1


def dot(x1, y1, x2, y2):
    return x1*x2 + y1*y2

n = int(input())
for i in range(n):
    isoceles = False
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    if (x1, y1) == (x2, y2) or (x1, y1) == (x3, y3) or (x2, y2) == (x3, y3):
        print(f"Case #{i+1}: not a triangle")
        continue
    v1 = (x2-x1, y2-y1)
    v2 = (x3 - x1, y3 - y1)
    v3 = (x3 - x2, y3 - y2)

    if cross(*v1, *v2) == 0:
        print(f"Case #{i+1}: not a triangle")
        continue
    l1 = sqrt(v1[0]**2 + v1[1]**2)
    l2 = sqrt(v2[0]**2 + v2[1]**2)
    l3 = sqrt(v3[0]**2 + v3[1]**2)
    if l1 + l2 < l3 or l1 + l3 < l2 or l2 + l3 < l1:
        print(f"Case #{i+1}: not a triangle")
        continue
    if l1 == l2 or l1 == l3 or l2 == l3:
        isoceles = True
    
    theta1 = round(degrees(acos(dot(*v1, *v2)/(l1*l2))), 1)
    theta2 = round(degrees(acos(dot(*(-v1[0], -v1[1]), *v3)/(l1*l3))), 1)
    if theta1 == 90 or theta2 == 90 or (180 - theta1 - theta2) == 90:
        print(f"Case #{i+1}: {('scalene','isosceles')[isoceles]} right triangle")
    elif theta1 > 90 or theta2 > 90 or (180 - theta1 - theta2) > 90:
        print(f"Case #{i+1}: {('scalene','isosceles')[isoceles]} obtuse triangle")
    else:
        print(f"Case #{i+1}: {('scalene','isosceles')[isoceles]} acute triangle")