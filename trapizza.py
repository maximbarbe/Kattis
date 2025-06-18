from math import pi
d = int(input())
a = int(input())
b = int(input())
h = int(input())

area_m = pi * (d/2)**2
area_t = ((a+b)*h)/2
if area_m > area_t:
    print('Mahjong!')
elif area_m < area_t:
    print('Trapizza!')
else:
    print("Jafn storar!")