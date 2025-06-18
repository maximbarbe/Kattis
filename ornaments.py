from math import pi,sqrt, radians, acos
import decimal
decimal.getcontext().prec = 100
while True:
    r, h, s = map(int, input().split(" "))
    if r == 0 and h == 0 and s == 0:
        break
    length = decimal.Decimal(2*pi * r * ((360 - 2*acos(r/h)*(180/pi))/360)+ 2*sqrt(h**2 - r**2))
    print(round(length + length * s /100, 2))