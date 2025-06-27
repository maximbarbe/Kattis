from math import cos, sin, tan, sqrt, atan ,degrees

d,x,y,h = map(int, input().split())

theta1 = atan((y+h/2)/x)
theta2 = atan((y-h/2)/x)
theta3 = atan(y/x)
theta4 = theta3 - theta2
theta5 = theta1 - theta3

print(d*tan(theta4) + d*tan(theta5))