from math import gcd
a, b = map(int,input().split("/"))
numerator = 5*a - 160*b
denominator = 9*b
if numerator == 0:
    print("0/1")
else:
    g = gcd(numerator, denominator)
    numerator //= g
    denominator //= g
    print(f"{numerator}/{denominator}")