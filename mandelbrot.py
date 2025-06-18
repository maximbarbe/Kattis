import sys
from math import sqrt
count = 0
for line in sys.stdin:
    count += 1
    x, y, r = map(float, line.split())
    zn = 0
    c = complex(x+y*1j)

    for i in range(int(r)):
        if sqrt(zn.real ** 2 + zn.imag**2) >= 2:
            print(f"Case {count}: OUT")
            break
        zn = zn.real**2 - zn.imag**2 + 2*zn.real*zn.imag*1j + c
    else:
        if sqrt(zn.real ** 2 + zn.imag**2) >= 2:
            print(f"Case {count}: OUT")
            
        else:
            print(f"Case {count}: IN")